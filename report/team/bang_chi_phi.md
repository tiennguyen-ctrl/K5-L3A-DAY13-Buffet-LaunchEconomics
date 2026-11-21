# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (ĐẠT; bằng 1/p vì k triệt tiêu) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token (mọi lần chạy) | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool (5.600 lần gọi) | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại (890 phút) | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại (1.132 phút) | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp 4.472 / 274,7 = **16,3 lần** hoá đơn chia số yêu cầu [simulated].
- Khoản lớn nhất là **làm lại: 51,8%** tổng chi phí [simulated]; tiếp theo là xem lại 40,7% [simulated]. Giờ nhân viên chiếm 92,5%.
- Lưu ý: 4.472 đ chỉ chia cho việc trợ lý làm xong, chưa tính 148 ca `chuyen_nhan_vien`. So với nhân viên tự làm, dùng chi phí cả hệ thống: (4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- **quoc_te không đáng để trợ lý xử lý** (1,88× so với 12.000 đ, thành công 27,3%) [simulated]. Chạy lại không giúp: tỉ lệ ok theo lần thử là 30,0% → 11,4% → 2,2%, lỗi lặp lại trên cùng yêu cầu nên chỉ tốn thêm tiền.
- doi_tac sát ngưỡng (0,85×) và có điều khoản riêng, nên cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Chi phí mỗi việc thành công trong phạm vi chưa cộng cố định là 3.414 đ [simulated] (cách tính: 40.000.000 / 33.750 = 1.185 đ).
- Chi phí cố định **không đổi kết luận** ở cả hai khối lượng (0,38× và 0,48× đều dưới 1), nhưng tăng gấp đôi (1.185 → 2.370 đ/việc) khi khối lượng nhỏ, nên hồ sơ phải nói rõ số đã cộng cố định ở khối lượng nào.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Gốc (A2) | Không đổi | 4.472 đ [simulated] | |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (5,6 + 40,7) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%) [simulated]. Giá token chỉ +5,6%, nên pilot phải theo dõi tỉ lệ làm lại và xem lại, không phải giá token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay). Mọi số có nhãn simulated.

- Giới hạn **2 lần rẻ nhất cho công ty** (6.901.220 đ), nhưng **không trùng** với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ). Tối ưu riêng chi phí mỗi việc thành công sẽ đẩy thêm 85 việc (319 − 234) sang nhân viên.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`, 982 yêu cầu): 10.568.513 đ / 900 việc = **11.743 đ = 0,98×** của 12.000 đ [simulated] (948 yêu cầu × 5 phút xem lại, 48 ca làm lại × 9 phút, token + tool 224.513 đ).
- Nếu dùng phút làm lại thật trong dữ liệu (15,3 phút/ca thay vì 9): **12.415 đ = 1,03×** [simulated], tức xem lại 100% đắt hơn nhân viên tự làm. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (làm lại 15,3 phút).
- Ý nghĩa: xem lại 100% thì trợ lý gần như không tiết kiệm được gì, vì tiền xem lại chiếm khoảng 90% chi phí. Pilot phải học được tỉ lệ xem lại có thể giảm an toàn xuống mức nào, và mỗi lần xem lại có ngắn hơn 5 phút được không.

## Kiểm số

- Người kiểm số: Phan Nhật Trường (độc lập với người viết code Nguyễn Trần Tiến).
- **A2:** Trường tính tay đối chiếu với `python lab13.py`, xác nhận **khớp** (lệch không quá 2%).
- **B1:** Trường kiểm quan hệ "giảm một nửa = nửa mức tăng của gấp đôi" (5,6 → 2,8; 40,7 → 20,3), xác nhận **khớp**.
- Xác nhận qua nhóm chat của nhóm. Trường bổ sung cách tính tay cụ thể tại đây nếu cần.
