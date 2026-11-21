# Phân công công việc — Lab 13 (LogiX-VN, Gate 2a)

Căn cứ: [README.md](README.md), [CHECKPOINTS.md](CHECKPOINTS.md), [RUBRIC.md](RUBRIC.md), [SUBMISSION.md](SUBMISSION.md), [RULES.md](RULES.md), [report/team/README.md](report/team/README.md), [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

## 1. Dự án hôm nay làm gì (tóm tắt)

Dựng **hồ sơ launch v0** cho trợ lý hoàn phí của LogiX-VN (dữ liệu giả lập, offline, không cần API key) rồi bảo vệ trước nhóm khác đóng vai hội đồng **Gate 2a**. Hồ sơ trả lời 4 câu hỏi: có đáng chạy không (chi phí mỗi việc thành công), nhân viên có dùng không (chỉ số), khi hỏng thì sao (bảng lỗi), pilot thiết kế thế nào (cỡ mẫu, đối chứng, luật dừng). Chấm: 70 điểm đối chiếu đáp án (A 20, B 15, C 10, D 15, E 10) + 30 điểm hội đồng (C6–C8).

Năm nhiệm vụ: **A** mô hình chi phí → **B** bảng độ nhạy → **C** bảng lỗi (gắn nhãn 20 ca) → **D** `pilot_plan.yaml` → **E** chỉ số, rủi ro, hồ sơ launch v0 → duyệt chéo → đóng gói.

## 2. Vai trò (theo 4 vai bắt buộc trong [TEAM.md](TEAM.md))

| Thành viên | MSSV | Trước giải lao (A, B) | Sau giải lao (D, E) | Có viết code? |
| --- | --- | --- | --- | --- |
| **Nguyễn Trần Tiến** (nhóm trưởng) | 2A202603504 | **Người viết code** | Người kiểm số | Có |
| **Phan Nhật Trường** | 2A202603459 | Người kiểm số | **Người viết code** | Có |
| **Nguyễn Ngọc Sang** | 2A202603444 | **Người gắn nhãn 1** (đọc đề, theo dõi "Xong khi") | Người gắn nhãn 1 | Không |
| **Đào Thị Thu Phương** | 2A202603457 | **Người gắn nhãn 2 kiêm giữ hồ sơ** (điền `ho_so_launch_v0.md` từ đầu buổi) | Giữ hồ sơ | Không |

- Quy định đề bài: **đổi người viết code sau giải lao (15:20–15:35)** để ít nhất hai người tự tay tính được chi phí. Tiến viết code A, B; Trường viết code D, E. Cả hai đều phải tự giải thích được công thức khi hội đồng hỏi.
- Sang và Phương **không viết code**, nhưng là hai người gắn nhãn độc lập ở CP3 (bắt buộc) và phụ trách phần chữ của hồ sơ (người phụ trách, luật dừng, event, rủi ro, hồ sơ launch).
- Nhóm trưởng (Tiến) thêm: tạo repo nhóm, push, kiểm checklist nộp, nhắc cả nhóm nộp link trên LMS.

## 3. Phân công theo file

| File | Người điền chính | Người kiểm / hỗ trợ | Phụ thuộc vào |
| --- | --- | --- | --- |
| `src/lab13.py` | Tiến (A, B) → Trường (D1, E1) | Trường kiểm A–B; Tiến kiểm D–E | |
| `report/team/bang_chi_phi.md` | Tiến (A, B) | Trường (đối chiếu tay, điền cột kiểm) | Output `lab13.py` |
| `report/team/bang_loi.md` | Sang + Phương (nhãn độc lập, quy tắc, bảng khắc phục) | Tiến, Trường rà cột "phát hiện đo được" | 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`; số từ A (xem mục C) |
| `report/team/pilot_plan.yaml` | Trường (D1, các trường số) + Phương (luật dừng, owner, D2) | Sang rà đúng mẫu NẾU–TRONG–THÌ–KHÔNG THÌ; Tiến chạy kiểm `yaml.safe_load` | D1 của Trường; số A/B của Tiến |
| `report/team/chi_so.md` | Trường (tính 3 chỉ số) + Sang (event, chỉ số tự đề xuất) + Phương (rủi ro kinh tế) | Tiến kiểm số rủi ro khớp bảng độ nhạy | Bảng B1, B4, A4 |
| `report/team/ho_so_launch_v0.md` | **Phương** | Sang rà từng mục; Tiến, Trường cấp số | Mọi file trên |
| `report/team/phieu_cham.md` | Sang + Phương (viết) | Tiến, Trường kiểm số nhóm bạn | Hồ sơ nhóm n + 1 |
| `report/team/group_report.md` | Tiến (khung, mục 3–4) | Phương (mục 5–8), Sang, Trường góp ý | Mọi file |
| `TEAM.md` | Tiến | Mọi người tự điền mục cá nhân | |
| `report/team/<MSSV>_<HoTen>.md` (4 file) | Từng người tự điền | | Xem mục 6 |

## 4. Quy ước chờ nhau

Ký hiệu: **[CHỜ X: gì]** = không làm tiếp phần này khi chưa nhận được thứ đó. **[GIAO X: gì]** = bàn giao cho X khi xong.

## 5. Kế hoạch chi tiết theo checkpoint

### 14:00 — Khởi động (10 phút)

| Ai | Việc |
| --- | --- |
| **Tiến** | Fork repo, đổi tên `K5-L3A-DAY13-TenNhom-LaunchEconomics`, mời 3 bạn. Chốt tên nhóm, điền phần "Thông tin nhóm" và bảng vai trong `TEAM.md`. |
| **Trường, Sang, Phương** | Clone **repo nhóm** (không clone repo đề). Tạo venv, `pip install -r src/requirements.txt`, chạy `python lab13.py` trong `src/` (sẽ báo NotImplementedError là bình thường). |
| **Phương** | Mở sẵn `ho_so_launch_v0.md`, ghi 7 mục + trạng thái "Chưa". Lập bảng theo dõi tiến độ (mục 8 bên dưới). |
| **Sang** | Đọc `CHECKPOINTS.md` + `RUBRIC.md`, lập danh sách "Xong khi" của A–E, đọc nhanh 20 ca lỗi trong docx (chưa gắn nhãn). |

**[GIAO]** Tiến → cả nhóm: URL repo nhóm. Nhóm xong khi cả 4 máy chạy được `python lab13.py`.

### CP1 · A — Mô hình chi phí (14:10 → 14:53)

| Bước | Ai | Việc | Ra sản phẩm |
| --- | --- | --- | --- |
| A1 | **Tiến** | Viết 3 hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` ở `TODO CP1`. Chạy ra 1,20 · 1,25 · 1,25. | 3 phép thử ĐẠT |
| | Trường | Tính tay ba số p = 0,8 để đối chiếu. | Giấy nháp / ảnh |
| | | **[GIAO Tiến → Trường]** báo "ĐẠT". **Chưa ai làm A2 khi chưa đạt cả ba.** | |
| A2 | **Tiến** | Viết `mo_hinh(runs, reqs, …)`; đọc CSV với `keep_default_na=False`. | Bảng A2 (9 dòng) |
| | **Trường** | Tính tay một con số độc lập (ví dụ phần token của 1 request, hoặc chi phí xem lại = 890 phút × 2.000 đ) để đối chiếu. | Số kiểm tay |
| | | **[CHỜ Tiến: bảng A2 từ output]** rồi so với số kiểm tay; lệch ≤ 2% thì báo "khớp". | |
| A3 | **Tiến** | Gọi `mo_hinh` cho từng `loai`; tính tỉ lệ ok theo từng lần thử (quoc_te: 30% → 11,4% → 2,2%). | Bảng A3 (4 dòng) |
| A4 | **Tiến** | Cộng chi phí cố định 40 triệu/tháng cho noi_dia + hang_nang. | Số A4 |
| Ghi | **Tiến + Trường** | Điền bảng A2, A3, A4 và câu trả lời vào `bang_chi_phi.md`; mọi số từ cột `_simulated` ghi nhãn `simulated`. | `bang_chi_phi.md` (phần A) |
| Hồ sơ | **Phương** | **[CHỜ Tiến: số A2, A3, A4]** → điền mục 1 (chi phí mỗi việc thành công), mục 3 (so với 12.000 đ; nhớ dùng số cả hệ thống 5.865 đ = 0,49×, không viết 0,37× nếu chưa cộng phần chuyển nhân viên). Trạng thái: **Giả lập**. | Mục 1, 3 của hồ sơ |
| Song song | **Sang** | **Chưa có việc cần code.** Đọc kỹ 5 loại lỗi Google PAIR và bảng "quy tắc cho ca dễ lẫn"; chuẩn bị mẫu ghi nhãn (bảng 20 dòng, cột nhãn, cột lý do) trong `bang_loi.md`. | Mẫu bảng nhãn |

Đối chiếu khi giảng viên chiếu slide chữa: Tiến báo lệch/không lệch cho cả nhóm. Số đáp án để so: cps 4.472 đ (16,3× hoá đơn token), 978 việc thành công, 4.373.585 đ tổng.

### CP2 · B — Bảng độ nhạy (14:53 → 15:20)

| Bước | Ai | Việc |
| --- | --- | --- |
| B1 | **Tiến** | Chạy 9 kịch bản bằng `mo_hinh` (token ×2/÷2, xem lại ×2/÷2, làm lại ×2/÷2, lương +25%, tối đa 2 lần, 1 lần). |
| | **Trường** | **[CHỜ Tiến: bảng B1]** → kiểm "giảm một nửa = nửa mức tăng của gấp đôi" (5,6 → 2,8; 40,7 → 20,3). |
| B2 | **Tiến** | Đổi cặp (token ×2 + xem lại ×2) → +46,3% = tổng hai tác động riêng; xếp hạng 3 yếu tố (làm lại · xem lại · lương). |
| B3 | **Tiến** | Giới hạn 1/2/3 lần chạy, chi phí cả hệ thống (2 lần rẻ nhất cho công ty, 1 lần thấp nhất cho cps). |
| B4 | **Tiến** | Kịch bản xem lại 100% cho noi_dia + hang_nang; nêu cả hai số (9 phút → 0,98×; 15,3 phút → 1,03×). |
| Ghi | **Tiến + Trường** | Điền bảng B1–B4 vào `bang_chi_phi.md` (mỗi câu trả lời ≤ 3 dòng, có số). |
| Hồ sơ | **Phương** | **[CHỜ Tiến: xếp hạng 3 yếu tố, B3, B4]** → điền mục 2 (ba yếu tố nhạy nhất), nháp mục 7 (rủi ro kinh tế). Trạng thái: Giả lập. |

**[GIAO Tiến → Sang, Phương]** nói "B xong" lúc ~15:15 để hai người chuẩn bị gắn nhãn. **15:20–15:35 giải lao; trong lúc nghỉ Tiến và Trường đổi vai** (Trường mở `lab13.py` đã có A, B, sẵn sàng viết D).

### CP3 · C — Bảng lỗi và cách khắc phục (15:35 → 16:08)

Đây là nhiệm vụ yêu cầu **hai người gắn nhãn độc lập** (Sang, Phương). Tiến và Trường hoàn thiện CP2 nếu còn thiếu rồi chuyển sang chuẩn bị D.

| Phút | Ai | Việc |
| --- | --- | --- |
| 0–8 | **Sang, Phương** | Ngồi tách nhau, **không trao đổi**, mỗi người gắn nhãn 20 ca (Do người dùng / Hệ thống / Ngữ cảnh / Giới hạn hệ thống / Ngầm) theo **nguyên nhân gốc**. Mỗi người tự ghi nhãn vào bản riêng, không mở file của người kia. |
| | **Tiến, Trường** | Chốt nốt B (nếu thiếu); Trường đọc yêu cầu D1 và dựng hàm `co_mau`. |
| 8–11 | **Sang + Phương** | **[CHỜ nhau: cả hai nộp xong bộ nhãn]** rồi so; tính đồng thuận = số ca trùng ÷ 20. **Không sửa bộ nhãn độc lập sau khi đã so.** |
| 11–16 | **Sang + Phương** | Với ca không trùng: thống nhất nhãn, ghi **một câu quy tắc phân biệt**. Dưới 16/20 → viết lại định nghĩa trước khi đi tiếp. |
| 16–30 | **Sang + Phương** | Chọn 5 ca (mỗi loại một ca), điền bảng khắc phục: phát hiện đo được (event, ngưỡng, tần suất) + **một vai trò** phụ trách (không ghi "cả đội"). Chia: Sang làm 3 ca, Phương làm 2 ca, rồi chéo nhau đọc lại. |
| | **Tiến** | **[CHỜ Sang + Phương: bảng khắc phục]** → rà: event dùng trong cột "phát hiện" có nằm trong danh sách 10 event mẫu không. |
| | **Phương** | Điền mục 5 (bảng lỗi) của hồ sơ, trạng thái: Xong, có bằng chứng. |

**[GIAO Sang/Phương → Tiến, Trường]**: danh sách vai trò phụ trách đã dùng (PM trợ lý hoàn phí, Kỹ sư trưởng agent, Trưởng nhóm CSKH, Kế toán trưởng…) để D dùng cùng bộ tên vai trò.

### CP4 · D — pilot_plan.yaml (16:08 → 16:36)

| Bước | Ai | Việc | Chờ ai / gì |
| --- | --- | --- | --- |
| D1 | **Trường** (người viết code) | Viết `co_mau`, tính 5 câu D1: (a) 1.251 · (b) 3.103/nhóm, cần 84 người > 40 · (c) tối đa 1.000 < 1.251 · (d) tối đa 300 · (e) m ≥ 299. Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (4,25%; phạm vi 3,97%). | Không |
| | **Tiến** (người kiểm số) | Tính tay câu (e): 20m ≥ 859 × (0,98 + 0,02m) → m ≥ 298,5 → 299. | **[CHỜ Trường: số D1]** để đối chiếu |
| D2 | **Phương** | Trả lời 5 câu "tách được tác động" (đối chứng cùng thời gian; ngẫu nhiên có seed; ảnh hưởng gián tiếp; viết trước; ≥ 20 cụm/nhóm). | **[CHỜ Trường: D1]** để biết có đủ 20 cụm không |
| Luật dừng | **Phương** (nháp) + **Sang** (rà) | Viết ≥ 3 luật dừng (an toàn, chi phí, mức sử dụng), đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng, thời hạn, người có quyền dừng. | **[CHỜ Trường: 4,25% mở lại]** để không đặt ngưỡng dừng ngay tuần đầu; **[CHỜ Tiến: số cps/B4]** cho luật chi phí |
| Ghi | **Trường** | Điền các trường số vào `pilot_plan.yaml`; ghi D1, D2 vào chú thích đầu file; xoá mọi dấu `?`. | Luật dừng từ Phương/Sang |
| Kiểm | **Tiến** | Chạy `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` và `grep -v '^ *#' ../report/team/pilot_plan.yaml \| grep -n '?'` (phải không in gì). Có ≥ 20 cụm mỗi nhóm hoặc ghi rõ đánh đổi. | **[CHỜ Trường + Phương: file hoàn chỉnh]** |
| Hồ sơ | **Phương** | Điền mục 6 (pilot plan). Nêu cả con số bất lợi: power 0,64 nếu tác động thật chỉ 5 điểm. | File YAML đã qua kiểm |

### CP5 · E — Chỉ số, rủi ro, hồ sơ launch v0 (16:36 → 17:00)

| Việc | Ai | Chờ ai / gì |
| --- | --- | --- |
| Tính thử 3 chỉ số: chính 82,83% (994/1.200), dùng 27,12% (48/177), an toàn 4,25% (51/1.200) | **Trường** (code), **Tiến** (kiểm số) | |
| Đề xuất thêm 1 chỉ số dùng + 1 chỉ số an toàn (mục "tự đề xuất") | **Sang** | |
| Danh sách ≥ 6 event có `trace_id`; kiểm chéo: mỗi chỉ số tính được từ event nào | **Sang** (viết), **Tiến** (kiểm chéo) | **[CHỜ Trường: 3 chỉ số]** |
| ≥ 2 dòng rủi ro kinh tế (số lấy từ bảng độ nhạy: làm lại ×2 → +51,8%; xem lại 100% → 0,98×/1,03×; khối lượng thấp → cố định +2.370 đ/việc) có đủ dấu hiệu theo dõi, hành động, người phụ trách | **Phương** | **[CHỜ Tiến: B1, B4, A4]** |
| Hoàn thiện `ho_so_launch_v0.md`: 7 mục, mỗi mục có con số chính + trạng thái (Xong, có bằng chứng · Chưa · Giả lập) + người phụ trách là một vai trò | **Phương** | **[CHỜ mọi người: số cuối]** |
| Viết dòng cuối: đề xuất **Go / Go có điều kiện / No-go**, kèm điều kiện, người phụ trách, ngày kiểm tra | **Phương + Sang đề xuất, Tiến (nhóm trưởng) chốt** | Số bất lợi: xem lại 100% = 0,98×; power 0,64; mở lại 4,25% |
| Rà "production": `grep -rni production ../report/team` không in gì | **Tiến** | |

**Hạn 17:00:** Phương gửi hồ sơ cho nhóm hội đồng (nhóm n chấm nhóm n + 1).

### 17:00 — Duyệt chéo Gate 2a (45 phút)

| Phút | Ai | Việc |
| --- | --- | --- |
| 17:00–17:10 | **Phương** | Gửi hồ sơ nhóm mình cho nhóm hội đồng. |
| 17:10–17:25 | **Sang + Phương** | Đọc hồ sơ nhóm n + 1, điền `phieu_cham.md` (3 tiêu chí 0/5/10, quyết định Go / Go có điều kiện / No-go kèm lý do có số, một câu hỏi). Chấm theo bằng chứng, không theo cách trình bày. |
| | **Tiến + Trường** | Kiểm số của nhóm bạn (chi phí, cỡ mẫu, nhãn `simulated`); báo Sang/Phương số nào lệch. |
| 17:25–17:40 | **Tiến** đại diện trình bày (1 phút) | Trường trả lời câu hỏi về tính toán, Phương/Sang trả lời về lỗi, pilot. Mỗi người chuẩn bị trả lời: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm thành công; cỡ mẫu hiệu dụng khi chia theo cụm; lý do đề xuất cuối. |
| | **Phương** | Ghi câu hỏi hội đồng hỏi và câu trả lời của nhóm vào `phieu_cham.md` / `group_report.md`. |

### 17:45 — Đóng gói, commit, push (15 phút, hạn nộp tại lớp 18:00; deadline cuối 23h59 GMT+7)

| Ai | Việc |
| --- | --- |
| **Phương** | Hoàn thiện `group_report.md` mục 5–8 (khó khăn, hạn chế, tài liệu tham khảo). |
| **Tiến** | `group_report.md` mục 1–4; điền bảng đóng góp trong `TEAM.md`. |
| **Mỗi người** | Copy `report/team/MSSV_HoTen.md` thành file riêng và điền (mục 6). |
| **Trường** | Chạy lại `python lab13.py` từ đầu đến cuối trên máy mình, xác nhận ba phép thử ĐẠT. |
| **Tiến** | Đi qua checklist ở [SUBMISSION.md](SUBMISSION.md#checklist), `git add`, commit, push (không commit `.venv/`, `.env`); ghi URL repo, nhánh, commit chốt vào `TEAM.md`. **Không force-push.** |
| **Cả 4 người** | Mỗi người **tự nộp link repo nhóm trên LMS bằng tài khoản cá nhân** trước 23h59 GMT+7 (ai không nộp thì không có điểm). |

## 6. Báo cáo cá nhân (mỗi người một file)

| Người | Tên file | Nội dung chính cần ghi |
| --- | --- | --- |
| Nguyễn Trần Tiến | `report/team/2A202603504_NguyenTranTien.md` | Code A, B; chi phí, độ nhạy; điều phối, nộp bài; công cụ AI đã dùng + cách tự kiểm |
| Nguyễn Ngọc Sang | `report/team/2A202603444_NguyenNgocSang.md` | Bộ nhãn độc lập CP3; bảng khắc phục; danh sách event, chỉ số đề xuất; phiếu chấm |
| Đào Thị Thu Phương | `report/team/2A202603457_DaoThiThuPhuong.md` | Bộ nhãn độc lập CP3; luật dừng, D2; hồ sơ launch v0; rủi ro kinh tế; group_report |
| Phan Nhật Trường | `report/team/2A202603459_PhanNhatTruong.md` | Kiểm số A, B; code D1, E1; cỡ mẫu; `pilot_plan.yaml` |

Theo [RULES.md](RULES.md): mỗi người ghi công cụ AI đã dùng và cách tự kiểm tra. Không dùng AI để bịa số, nhãn lỗi hay kết quả duyệt chéo.

## 7. Quy tắc cả nhóm phải nhớ

1. Qua đủ ba phép thử A1 (1,20 · 1,25 · 1,25) rồi mới làm tiếp.
2. Mọi số tính từ hai cột `_simulated` ghi nhãn **simulated**.
3. Mỗi câu trả lời không quá 3 dòng, có ít nhất một con số.
4. Không dùng từ "production" trong hồ sơ.
5. Người phụ trách luôn là **một vai trò**, không ghi "cả đội".
6. Nhãn lỗi: gắn độc lập, so sau, không sửa bộ độc lập.
7. Không sửa `src/logix_runs.csv`, `src/logix_requests.csv`; luôn đọc CSV với `keep_default_na=False`.
8. Viết "chỉ số trong đợt chạy thử là…", không viết "trợ lý đã nâng chỉ số".

## 8. Bảng theo dõi tiến độ (Phương cập nhật)

| Mốc | Hạn | Người chính | Người chờ | Trạng thái |
| --- | --- | --- | --- | --- |
| Repo + môi trường | 14:10 | Tiến | Cả nhóm | |
| A1 ĐẠT | 14:20 | Tiến | Trường | |
| A2–A4 + `bang_chi_phi.md` (A) | 14:53 | Tiến, Trường | Phương | |
| B1–B4 | 15:20 | Tiến, Trường | Phương | |
| Đổi người viết code | 15:35 | Tiến ↔ Trường | | |
| Hai bộ nhãn độc lập | 15:43 | Sang, Phương | | |
| Đồng thuận + bảng khắc phục | 16:08 | Sang, Phương | Tiến (rà) | |
| D1 + D2 | 16:20 | Trường, Phương | Tiến (kiểm số) | |
| `pilot_plan.yaml` không còn `?` | 16:36 | Trường, Phương | Tiến (chạy kiểm) | |
| `chi_so.md` | 16:50 | Sang, Trường, Phương | Tiến | |
| `ho_so_launch_v0.md` đủ 7 mục + đề xuất | 17:00 | Phương | Cả nhóm | |
| Phiếu chấm nhóm bạn | 17:25 | Sang, Phương | Tiến, Trường | |
| Push + nộp LMS | 18:00 (tối đa 23h59) | Tiến, cả nhóm | | |
