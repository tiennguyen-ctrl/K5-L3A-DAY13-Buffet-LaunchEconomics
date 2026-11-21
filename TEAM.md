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
- [Báo cáo nhóm](report/team/group_report.md): rà bổ sung sau commit trên; mã commit của lần bổ sung sẽ ghi khi lưu vào Git.

## Đào Thị Thu Phương - 2A202603457

### Phần việc phụ trách

- Gắn nhãn độc lập CP3; giữ hồ sơ `ho_so_launch_v0.md`; luật dừng, D2, rủi ro kinh tế; group_report.

### Đóng góp cụ thể

- (điền cuối buổi)

### Bằng chứng

- (commit, file, output)
