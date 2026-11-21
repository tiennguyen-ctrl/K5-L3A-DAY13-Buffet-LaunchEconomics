"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


# ---------- Nhiệm vụ D1 · Cỡ mẫu pilot ----------
def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm để so sánh hai tỉ lệ với kiểm định hai phía."""
    chuan = NormalDist()
    z_alpha = chuan.inv_cdf(1 - alpha / 2)
    z_power = chuan.inv_cdf(power)
    p_trung_binh = (p1 + p2) / 2
    sd_gop = math.sqrt(2 * p_trung_binh * (1 - p_trung_binh))
    sd_rieng = math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((z_alpha * sd_gop + z_power * sd_rieng) / (p2 - p1)) ** 2)


def in_co_mau_pilot(reqs):
    baseline, muc_tieu_5_diem, muc_tieu_6_diem = 0.70, 0.75, 0.76
    icc = 0.02
    nhan_vien_moi_nhom, depot_moi_nhom = 20, 6

    n_5_diem = co_mau(baseline, muc_tieu_5_diem)
    yeu_cau_moi_nguoi = 75
    de_75 = 1 + (yeu_cau_moi_nguoi - 1) * icc
    n_theo_nhan_vien = math.ceil(n_5_diem * de_75)
    so_nhan_vien_can = math.ceil(n_theo_nhan_vien / yeu_cau_moi_nguoi)

    n_6_diem = co_mau(baseline, muc_tieu_6_diem)
    # Giải c*m / (1 + (m - 1)*ICC) >= n theo m, với c = 20.
    m_toi_thieu = math.ceil(n_6_diem * (1 - icc) / (nhan_vien_moi_nhom - n_6_diem * icc))
    de_pilot = 1 + (m_toi_thieu - 1) * icc
    n_thuc_te = nhan_vien_moi_nhom * m_toi_thieu

    # Power xấp xỉ hai phía với Cohen's h và hai nhóm bằng nhau.
    chuan = NormalDist()
    z_alpha = chuan.inv_cdf(0.975)
    h_5_diem = 2 * (math.asin(math.sqrt(muc_tieu_5_diem)) - math.asin(math.sqrt(baseline)))
    dich_chuyen_z = h_5_diem * math.sqrt(n_6_diem / 2)
    power_5_diem = chuan.cdf(dich_chuyen_z - z_alpha) + chuan.cdf(-dich_chuyen_z - z_alpha)

    print('\nD1 · Cỡ mẫu pilot')
    print(f'a) Theo yêu cầu: {n_5_diem} yêu cầu mỗi nhóm.')
    print(f'b) Theo nhân viên, m = {yeu_cau_moi_nguoi}: DE = {de_75:.2f}, '
          f'{n_theo_nhan_vien} yêu cầu và {so_nhan_vien_can} nhân viên mỗi nhóm '
          f'({2 * so_nhan_vien_can} người so với {2 * nhan_vien_moi_nhom} người có sẵn).')
    print(f'c) Theo nhân viên: cỡ mẫu hiệu dụng < {nhan_vien_moi_nhom / icc:.0f} mỗi nhóm.')
    print(f'd) Theo depot: cỡ mẫu hiệu dụng < {depot_moi_nhom / icc:.0f} mỗi nhóm.')
    print(f'e) Chênh 6 điểm: cần {n_6_diem} yêu cầu hiệu dụng mỗi nhóm, '
          f'ít nhất {m_toi_thieu} yêu cầu mỗi nhân viên, DE = {de_pilot:.2f}.')
    print(f'   Mỗi nhóm có {n_thuc_te} yêu cầu thực tế, tương đương {n_thuc_te / de_pilot:.2f} hiệu dụng.')
    print(f'   Nếu tác động thật là 5 điểm, power xấp xỉ {power_5_diem:.2f}.')

    mo_lai = reqs['mo_lai_trong_7_ngay'].eq(1)
    trong_pham_vi = reqs['loai'].isin(['noi_dia', 'hang_nang'])
    in_ti_le('Mở lại trong 7 ngày (toàn bộ)', mo_lai.sum(), len(reqs))
    in_ti_le('Mở lại trong 7 ngày (nội địa + hàng nặng)',
             (mo_lai & trong_pham_vi).sum(), trong_pham_vi.sum())


# ---------- Nhiệm vụ E1 · Chỉ số trên dữ liệu chạy thử ----------
def tinh_chi_so_e1(reqs):
    """Trả về tử số và mẫu số của từng chỉ số."""
    dong_trong_24h = reqs['dong_trong_24h'].eq(1)
    khong_mo_lai = reqs['mo_lai_trong_7_ngay'].eq(0)
    mo_lai = reqs['mo_lai_trong_7_ngay'].eq(1)
    da_xem_lai = reqs['duoc_xem_lai'].eq(1)
    sua_hoac_bo = reqs['quyet_dinh_xem_lai'].isin(['sua', 'bo'])

    return {
        'Đóng trong 24 giờ và không mở lại trong 7 ngày': ((dong_trong_24h & khong_mo_lai).sum(), len(reqs)),
        'Bỏ qua gợi ý trong số yêu cầu đã xem lại': ((da_xem_lai & sua_hoac_bo).sum(), da_xem_lai.sum()),
        'Mở lại trong 7 ngày': (mo_lai.sum(), len(reqs)),
    }


def in_ti_le(ten, tu_so, mau_so):
    if mau_so == 0:
        print(f'{ten}: không xác định (không có yêu cầu).')
        return
    print(f'{ten}: {tu_so / mau_so:.2%} ({tu_so}/{mau_so})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu (số chi phí là simulated) ----------
    print('\nA3 · Theo loại yêu cầu [simulated]')
    print(f"{'loai':10s} {'so_yc':>6s} {'thanh_cong':>11s} {'lan_chay/yc':>12s} {'cps (d)':>9s} {'/12.000':>8s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        so_run = runs['request_id'].isin(r['request_id']).sum()
        print(f"{loai:10s} {len(r):6d} {kq['thanh_cong'] / len(r):11.1%} {so_run / len(r):12.2f} "
              f"{kq['cps']:9,.0f} {kq['cps'] / BASELINE:7.2f}x")
    print('\nA3 · Tỉ lệ ok theo từng lần thử (attempt)')
    ok = runs.merge(reqs[['request_id', 'loai']], on='request_id').assign(ok=lambda d: (d['status'] == 'ok').astype(int))
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    # ---------- Nhiệm vụ A4 · Cộng chi phí cố định (phạm vi pilot: noi_dia + hang_nang) ----------
    CO_DINH_THANG = 40_000_000
    YC_THANG = 45_000
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pv)
    viec_thang = YC_THANG * kq_pv['thanh_cong'] / len(reqs)
    co_dinh_moi_viec = CO_DINH_THANG / viec_thang
    co_dinh_nua = CO_DINH_THANG / (viec_thang / 2)
    print('\nA4 · Chi phí cố định, phạm vi noi_dia + hang_nang [simulated]')
    print(f'  cps trong phạm vi            {kq_pv["cps"]:8,.0f} đ')
    print(f'  việc thành công / tháng      {viec_thang:8,.0f}')
    print(f'  cố định mỗi việc             {co_dinh_moi_viec:8,.0f} đ')
    print(f'  cps + cố định                {kq_pv["cps"] + co_dinh_moi_viec:8,.0f} đ = {(kq_pv["cps"] + co_dinh_moi_viec) / BASELINE:.2f}x')
    print(f'  nếu khối lượng giảm một nửa  {kq_pv["cps"] + co_dinh_nua:8,.0f} đ = {(kq_pv["cps"] + co_dinh_nua) / BASELINE:.2f}x (cố định {co_dinh_nua:,.0f} đ/việc)')
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    in_co_mau_pilot(reqs)

    print('\nE1 · Chỉ số trong đợt chạy thử (dữ liệu giả lập)')
    for ten, (tu_so, mau_so) in tinh_chi_so_e1(reqs).items():
        in_ti_le(ten, tu_so, mau_so)
