# Báo cáo cá nhân — Nguyễn Trần Tiến - 2A202603504

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trần Tiến (nhóm trưởng)
- MSSV: 2A202603504
- Email: nguyentien2004abc@gmail.com
- Vai trong nhóm: người viết code (nhiệm vụ A, B); sau giải lao là người kiểm số (nhiệm vụ D, E). Nhóm trưởng: tạo repo, điều phối, push và nộp bài.

## 2. Phần việc phụ trách

- Tạo và quản lý repo nhóm Buffet, mời thành viên, chốt `TEAM.md` và kế hoạch phân công `PHAN_CONG.md`.
- Viết code `src/lab13.py` cho nhiệm vụ A (CP1) và B (CP2).
- Điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4).
- Sau giải lao: kiểm số D1 (tính tay cỡ mẫu), chạy kiểm `pilot_plan.yaml`, rà bảng khắc phục của hai người gắn nhãn, rà từ cấm (theo SUBMISSION.md) trước khi nộp, điền `group_report.md` mục 1–4.

## 3. Đóng góp cụ thể

- **A1:** viết ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử đáp án biết trước ĐẠT (1,20 · 1,25 · 1,25).
- **A2:** viết `mo_hinh(runs, reqs, …)`. Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ); 978 việc thành công.
- **A3:** tách theo loại yêu cầu. noi_dia 2.696 đ (0,22×), hang_nang 8.221 đ (0,69×), quoc_te 22.515 đ (1,88×), doi_tac 10.215 đ (0,85×) [simulated]. quoc_te không đáng để trợ lý xử lý và chạy lại không giúp (tỉ lệ ok 30,0% → 11,4% → 2,2%).
- **A4:** cộng chi phí cố định 40 triệu đ/tháng cho noi_dia + hang_nang: 4.599 đ = 0,38×; một nửa khối lượng 5.784 đ = 0,48× [simulated].
- **B1–B2:** chín kịch bản độ nhạy; xếp hạng 1. số ca làm lại (+51,8%), 2. tỉ lệ xem lại (+40,7%), 3. lương (+23,1%) [simulated].
- **B3:** giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ cả hệ thống), nhưng giới hạn 1 lần cho chi phí mỗi việc thành công thấp nhất (4.111 đ).
- **B4:** xem lại 100% cho noi_dia + hang_nang: 11.743 đ = 0,98×; nếu làm lại 15,3 phút/ca thì 12.415 đ = 1,03× [simulated].
- Gộp xung đột `src/lab13.py` khi cùng lúc với code D1, E1 của Trường: giữ cả hai phần, kết quả vẫn chạy đúng.

## 4. Bằng chứng

- Commit trên nhánh `main`: `d55cdc7` (A1 + `mo_hinh`), `15ec23d` (A3, A4 + bảng A), `663632b` (B1–B4 trong code), `8efbc0e` (bảng B + mục Kiểm số).
- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `TEAM.md`, `PHAN_CONG.md`.
- Chạy `python lab13.py` trong `src/` in ba phép thử ĐẠT và các bảng A2, A3, A4, B1–B4.
- Kiểm số độc lập: Phan Nhật Trường xác nhận khớp A2 và B1 (ghi ở mục "Kiểm số" của `bang_chi_phi.md`).
- Kiểm số D1 câu (e), tính tay: cần 859 yêu cầu hiệu dụng mỗi nhóm, 20 nhân viên mỗi nhóm. 20m / (1 + (m − 1) × 0,02) ≥ 859 → 20m ≥ 859 × (0,98 + 0,02m) = 841,82 + 17,18m → 2,82m ≥ 841,82 → m ≥ 298,5 → **m ≥ 299** yêu cầu mỗi nhân viên. Khớp code của Trường (299, DE = 6,96).

## 5. Công cụ AI đã dùng

- **Claude Code (Anthropic):** hỗ trợ lập kế hoạch phân công, gợi ý và viết code cho A1–A4 và B1–B4, điền bảng trong `bang_chi_phi.md`, gộp xung đột git.
- **Cách tự kiểm tra:**
  - Chạy `python lab13.py` trên máy mình, ba phép thử đáp án biết trước phải ĐẠT.
  - Đối chiếu từng số với số tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch không quá 2%).
  - Kiểm tra chéo "giảm một nửa = nửa mức tăng của gấp đôi" (5,6 → 2,8; 40,7 → 20,3).
  - Người kiểm số độc lập (Trường) tính tay đối chiếu A2 và B1.
- Mọi con số trong hồ sơ do `src/lab13.py` tính ra; không dùng AI để bịa số, nhãn lỗi hay kết quả duyệt chéo.

## 6. Tự đánh giá

- Làm tốt: A và B xong đúng hạn, số khớp đáp án, bàn giao sớm để Phương và Trường làm tiếp.
- Cần cải thiện: (điền cuối buổi sau khi hoàn thành phần kiểm số D, E và đóng gói).
