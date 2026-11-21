# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Ngọc Sang · Người gắn nhãn 2: Đào Thị Thu Phương (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Hai bộ nhãn trùng 20/20 ca, không có ca nào phải thống nhất lại. Bộ nhãn độc lập giữ nguyên, không sửa sau khi so.
- Quy tắc hai người cùng dùng: đầu vào hoặc thao tác sai của khách là **Do người dùng**; trợ lý làm sai chính sách, thiết kế hoặc báo sai trạng thái là **Hệ thống**; làm đúng nhưng lệch kỳ vọng hoặc hoàn cảnh của khách là **Ngữ cảnh**; thiếu năng lực, dữ liệu hoặc phạm vi là **Giới hạn hệ thống**; sai lệch tồn tại mà cả khách lẫn giám sát đều không thấy cho tới khi kiểm tra sau là **Ngầm**.
- Ca dễ lẫn: 06, 09 (khách nhập sai, trợ lý thêm thiếu sót không gợi ý sửa) và 13 (ngoài phạm vi, trợ lý thêm thiếu sót không báo giới hạn) gắn theo nguyên nhân gốc, không theo chỗ cần sửa; ca 15 là Hệ thống chứ không phải Ngầm vì nhân viên xem lại đã bắt được.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | Event `ticket_closed` do khách bấm "Xác nhận đã nhận tiền" khi `refund_ledger_write` chưa có ket_qua ghi có; đếm hằng ngày, ngưỡng 0 ca. Theo dõi thêm `ticket_reopened` trong 7 ngày sau khi đóng. | Chỉ hiện nút khi giao dịch đã ghi có; thêm bước xác nhận lần hai; cho khách hoàn tác trong 48 giờ. | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát `refund_ledger_write` theo mã đơn và loại quyền lợi hằng ngày; cảnh báo ngay khi một quyền lợi có hơn 1 giao dịch hoàn thành công (ngưỡng 0). | Bắt buộc `idempotency_key` cho mọi lần gọi ghi sổ; yêu cầu gửi lại trả về trạng thái giao dịch đã có. | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Đếm thông báo không khẩn cấp gửi trong khung 22:00–07:00 theo giờ khách (theo `ticket_closed.closed_at`), hằng tuần; mục tiêu 0 khi khách chưa chọn nhận ban đêm. | Đặt giờ yên lặng, xếp lịch gửi sáng hôm sau, cho khách chọn giờ nhận. | PM trợ lý hoàn phí |
| 11 | Giới hạn hệ thống | Đếm tin nhắn không phải văn bản (thoại, ảnh) theo tuần từ `refund_request_created`; đo tỉ lệ khách bỏ cuộc (không có `ticket_closed` trong 24 giờ) sau câu "vui lòng nhập bằng chữ". | Bổ sung chuyển giọng nói thành văn bản; trong lúc chưa có, trợ lý nói rõ chưa nghe được tin thoại, đưa nút chọn nhanh hoặc câu mẫu, hoặc `handoff_to_staff`. | Kỹ sư trưởng agent |
| 05 | Ngầm | `audit_sample_checked` hằng tuần: so so_tien_da_hoan với so_tien_dung (số thực trả sau giảm giá); cảnh báo mọi đơn hoàn vượt mức chính sách (ngưỡng 0). | Sửa cơ sở tính hoàn theo số thực trả; rà soát các đơn bị ảnh hưởng; bổ sung đối soát tự động hằng ngày. | Kế toán trưởng |
