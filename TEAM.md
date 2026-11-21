# Team

## Thông tin nhóm

- Tên nhóm: Buffet
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-Buffet-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: https://github.com/tiennguyen-ctrl/K5-L3A-DAY13-Buffet-LaunchEconomics
- Nhánh nộp: `main`; commit chốt: (điền sau khi push lần cuối)
- Phân công chi tiết, thứ tự chờ nhau: [PHAN_CONG.md](PHAN_CONG.md)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Trần Tiến (nhóm trưởng) | 2A202603504 | nguyentien2004abc@gmail.com | tiennguyen-ctrl | Người viết code (A, B) → Người kiểm số (D, E); điều phối, nộp bài |
|   2 | Phan Nhật Trường | 2A202603459 | Truong02052004@gmail.com | pnt0803 | Người kiểm số (A, B) → Người viết code (D, E) |
|   3 | Nguyễn Ngọc Sang | 2A202603444 | nguyenngocsang051003@gmail.com | ngocsangnguyen | Người gắn nhãn 1; event, chỉ số đề xuất, phiếu chấm (không viết code) |
|   4 | Đào Thị Thu Phương | 2A202603457 | phuongdtt1824@gmail.com | (điền) | Người gắn nhãn 2 kiêm giữ hồ sơ; luật dừng, hồ sơ launch v0 (không viết code) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Nguyễn Trần Tiến - 2A202603504

### Phần việc phụ trách

- Nhóm trưởng: tạo repo, push, nộp. Viết code `src/lab13.py` phần A, B; kiểm số D, E.

### Đóng góp cụ thể

- (điền cuối buổi)

### Bằng chứng

- (commit, file, output)

## Phan Nhật Trường - 2A202603459

### Phần việc phụ trách

- Kiểm số A, B; viết code D1, E1; `pilot_plan.yaml`.

### Đóng góp cụ thể

- Đối chiếu A2 và B1. Chi phí xem lại A2 là 890 phút × 2.000 đ = 1.780.000 đ [simulated]. Ở B1, mức giảm bằng một nửa mức tăng khi tính trước khi làm tròn.
- Triển khai D1 với hỗ trợ của Codex. Tính năm câu cỡ mẫu, tỉ lệ mở lại trong 7 ngày và điền thông số cỡ mẫu vào `pilot_plan.yaml`. Phương án chia theo nhân viên cần 20 người mỗi nhóm và ít nhất 299 yêu cầu mỗi người để phát hiện chênh lệch 6 điểm phần trăm.
- Triển khai E1 với hỗ trợ của Codex. Tính và ghi ba chỉ số chạy thử trên dữ liệu giả lập vào `chi_so.md` (82,83%, 27,12% và 4,25%).

### Bằng chứng

- [Bảng chi phí và mục Kiểm số](report/team/bang_chi_phi.md#kiểm-số)
- [Commit D1/E1 `8fec924`](https://github.com/tiennguyen-ctrl/K5-L3A-DAY13-Buffet-LaunchEconomics/commit/8fec9246cee26c2492d61cfd6d6b325decec0bc7) · [Mã tính toán](src/lab13.py) · [Kế hoạch pilot](report/team/pilot_plan.yaml) · [Bảng chỉ số](report/team/chi_so.md)
- [Báo cáo cá nhân](report/team/2A202603459_PhanNhatTruong.md)

## Nguyễn Ngọc Sang - 2A202603444

### Phần việc phụ trách

- Gắn nhãn độc lập CP3, bảng khắc phục; danh sách event, chỉ số đề xuất; phiếu chấm.

### Đóng góp cụ thể

- Soạn và rà hai chỉ số đề xuất, danh sách event cùng ánh xạ chỉ số–event trong `chi_so.md`, có ChatGPT/Codex hỗ trợ.
- Rà cách phát hiện và khắc phục năm ca trong `bang_loi.md`; phân biệt ghi sổ với ghi có, giờ đóng ticket với giờ gửi thông báo và bổ sung dữ liệu xử lý đầu vào không hỗ trợ.
- Rà luật dừng trong `pilot_plan.yaml`, tách hoàn trùng để dừng trong 30 phút và làm rõ thời gian theo dõi của chỉ số mở lại; đồng bộ hồ sơ launch.
- Rà báo cáo nhóm: cập nhật phần C–E, đề xuất Go có điều kiện và giới hạn cỡ mẫu hiệu dụng; tách kết quả duyệt chéo còn chờ khỏi đề xuất của nhóm.
- Chuẩn bị phiếu chấm; chưa chấm nhóm bạn do chưa có hồ sơ. Kết quả gắn nhãn độc lập cần đối chiếu hai bản gốc trước khi xác nhận.

### Bằng chứng

- [Báo cáo cá nhân và công cụ AI đã dùng](report/team/2A202603444_NguyenNgocSang.md).
- [Đặc tả chỉ số và event](report/team/chi_so.md), [bảng khắc phục](report/team/bang_loi.md), [luật dừng pilot](report/team/pilot_plan.yaml), [hồ sơ launch](report/team/ho_so_launch_v0.md).
- [Commit `17e8ae2` — Sangcommit](https://github.com/tiennguyen-ctrl/K5-L3A-DAY13-Buffet-LaunchEconomics/commit/17e8ae214c5aa6e74330bda7c3ae185ba08bf8a7): báo cáo cá nhân, đặc tả event, bảng khắc phục, luật dừng và hồ sơ liên quan.
- [Commit `8b424d9` — Sangcommit](https://github.com/tiennguyen-ctrl/K5-L3A-DAY13-Buffet-LaunchEconomics/commit/8b424d9d7326f1b62b89ed2cfb0df5ca8cd43d2c): cập nhật phần C–E, đề xuất và giới hạn cỡ mẫu trong [báo cáo nhóm](report/team/group_report.md); bổ sung hai chỉ số vào hồ sơ launch, đồng bộ trạng thái bằng chứng nhãn và chuẩn bị câu hỏi duyệt chéo.

## Đào Thị Thu Phương - 2A202603457

### Phần việc phụ trách

- Gắn nhãn độc lập CP3; giữ hồ sơ `ho_so_launch_v0.md`; luật dừng, D2, rủi ro kinh tế; group_report.

### Đóng góp cụ thể

- Giữ hồ sơ launch v0 từ đầu buổi: điền 7 mục khi có số (chi phí 4.472 đ, phạm vi pilot 0,38×, cả hệ thống 0,49×, ba yếu tố nhạy +51,8% · +40,7% · +23,1% [simulated]) và dòng đề xuất Go có điều kiện với 4 điều kiện, người phụ trách, ngày kiểm tra; sau đó thay bằng bản rút gọn của Tiến, ghi rõ ca 7. Có Claude Code hỗ trợ soạn nháp.
- Gắn nhãn độc lập 20 ca (người gắn nhãn 2); ghép hai bộ nhãn vào `bang_loi.md` (đồng thuận 20/20), viết quy tắc phân biệt, chọn ca 14, 11 cho bảng khắc phục.
- Viết D2 (5 câu tách được tác động) và nháp 3 luật dừng trong `pilot_plan.yaml`, đặt ngưỡng an toàn so với đối chứng vì mở lại hiện tại đã 3,97%; Sang rà và tách thành 4 luật.
- Viết 3 dòng rủi ro kinh tế trong `chi_so.md` E2 (làm lại ×2 +51,8%; xem lại 100% 0,98×; khối lượng một nửa +2.370 đ/việc [simulated]).
- Viết `group_report.md` mục 5, 7, 8; giải quyết xung đột merge ở `ho_so_launch_v0.md`.

### Bằng chứng

- [Báo cáo cá nhân và công cụ AI đã dùng](report/team/2A202603457_DaoThiThuPhuong.md).
- [Hồ sơ launch](report/team/ho_so_launch_v0.md), [bảng lỗi](report/team/bang_loi.md), [D2 và luật dừng](report/team/pilot_plan.yaml), [rủi ro kinh tế E2](report/team/chi_so.md), [báo cáo nhóm](report/team/group_report.md).
- [Commit `9c3659a`](https://github.com/tiennguyen-ctrl/K5-L3A-DAY13-Buffet-LaunchEconomics/commit/9c3659ae2df9ed714169a041ea4b3c12955b1549): hồ sơ 7 mục và đề xuất, `bang_loi.md`, D2 và luật dừng, E2.
- [Commit `0869544`](https://github.com/tiennguyen-ctrl/K5-L3A-DAY13-Buffet-LaunchEconomics/commit/086954449e46b9ca01b56f7ef19be35e3c2a7d15): `group_report.md` mục 5, 7, 8; hồ sơ mục 4; báo cáo cá nhân.
- [Commit `72152d1`](https://github.com/tiennguyen-ctrl/K5-L3A-DAY13-Buffet-LaunchEconomics/commit/72152d1f9b34af6e02c6d3c68bfe915b058cb5f7): merge với commit của Sang và Trường, giải quyết xung đột hồ sơ.
- [Commit `3b983b0`](https://github.com/tiennguyen-ctrl/K5-L3A-DAY13-Buffet-LaunchEconomics/commit/3b983b0c944d2df99cc0c55c71e62f36aaec28a5): hồ sơ bản rút gọn, hoàn thiện báo cáo cá nhân.
