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

**Bằng chứng bản gốc:** hai bộ nhãn riêng, chép nguyên văn, mỗi ca có lý do của từng người: [người gắn nhãn 1 · Sang](nhan_doc_lap/nhan_1_NguyenNgocSang.md) · [người gắn nhãn 2 · Phương](nhan_doc_lap/nhan_2_DaoThiThuPhuong.md). Hai cột nhãn ở bảng trên khớp từng ca với hai bản gốc; lý do của hai người viết khác nhau dù cùng nhãn. Mức 100% là kết quả so hai bản gốc này.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Hai bộ nhãn trùng 20/20 ca, không có ca nào phải thống nhất lại. Bộ nhãn độc lập giữ nguyên, không sửa sau khi so.
- Quy tắc hai người cùng dùng: đầu vào hoặc thao tác sai của khách là **Do người dùng**; trợ lý làm sai chính sách, thiết kế hoặc báo sai trạng thái là **Hệ thống**; làm đúng nhưng lệch kỳ vọng hoặc hoàn cảnh của khách là **Ngữ cảnh**; thiếu năng lực, dữ liệu hoặc phạm vi là **Giới hạn hệ thống**; sai lệch tồn tại mà cả khách lẫn giám sát đều không thấy cho tới khi kiểm tra sau là **Ngầm**.
- Ca dễ lẫn: 06, 09 (khách nhập sai, trợ lý thêm thiếu sót không gợi ý sửa) và 13 (ngoài phạm vi, trợ lý thêm thiếu sót không báo giới hạn) gắn theo nguyên nhân gốc, không theo chỗ cần sửa; ca 15 là Hệ thống chứ không phải Ngầm vì nhân viên xem lại đã bắt được.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | Nối `ticket_closed` có `closed_by=customer`, `close_reason=refund_received` với `refund_settlement_updated` theo `refund_id`; cảnh báo ngay và tổng hợp hằng ngày khi tại thời điểm đóng chưa có xác nhận `status=credited` từ ngân hàng/ví (mục tiêu 0 ca). Theo dõi thêm `ticket_reopened` trong 7 ngày sau đóng. | Chỉ cho xác nhận đã nhận tiền sau xác nhận ghi có của ngân hàng/ví; thêm bước xác nhận lần hai và cho hoàn tác trong 48 giờ. Nếu chưa có dữ liệu ghi có, giữ trạng thái chờ xác minh và cung cấp đường chuyển nhân viên. | PM trợ lý hoàn phí |
| 20 | Hệ thống | Theo dõi liên tục `refund_ledger_write` có `status=success`, nhóm theo `order_id` + `entitlement_id` trên toàn lịch sử; cảnh báo ngay khi có hơn 1 `refund_id` khác nhau cho cùng quyền lợi. Khử bản ghi lặp của cùng `refund_id`; đối soát lại hằng ngày, mục tiêu 0 quyền lợi hoàn trùng. | Bắt buộc `idempotency_key` ổn định theo đơn và quyền lợi cho mọi lần gọi ghi sổ, kể cả yêu cầu gửi lại có `request_id` mới; áp ràng buộc duy nhất tại sổ cái và trả về trạng thái giao dịch đã có. | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Từ `notification_sent`, đếm thông báo `channel=zalo`, `urgency=normal`, `overnight_opt_in=false` có `sent_at` đổi theo `customer_timezone` nằm trong [22:00, 07:00). Cảnh báo ngay mỗi lần gửi vi phạm và tổng hợp hằng tuần; mục tiêu 0. | Đặt giờ yên lặng, xếp lịch gửi từ 07:00 theo múi giờ khách và cho khách chọn giờ nhận; kiểm tra lại tùy chọn trước khi gửi. | PM trợ lý hoàn phí |
| 11 | Giới hạn hệ thống | Từ `assistant_input_rejected` có `reason=unsupported_input`, đếm hằng tuần các yêu cầu bị từ chối mà sau 24 giờ chưa có `customer_message_received` dạng `text` hoặc `handoff_to_staff`; chia cho tổng yêu cầu bị từ chối đã đủ 24 giờ theo dõi, mục tiêu 0%. Đây là chỉ báo chưa tiếp tục được, cần kiểm tra hội thoại trước khi kết luận bỏ cuộc. | Bổ sung chuyển giọng nói thành văn bản; trong lúc chưa có, nói rõ giới hạn, đưa câu mẫu nhập chữ và lựa chọn chuyển nhân viên; ghi nhận lần từ chối và cách hỗ trợ tiếp tục. | Kỹ sư trưởng agent |
| 05 | Ngầm | Từ `audit_sample_checked` hằng tuần, so `actual_amount_vnd` với `expected_amount_vnd` theo `policy_version`, tính trên số thực trả sau giảm giá; cảnh báo mọi khoản hoàn vượt mức chính sách (mục tiêu 0 ca). | Sửa cơ sở tính hoàn theo số thực trả; rà soát các đơn bị ảnh hưởng; bổ sung đối soát tự động hằng ngày. | Kế toán trưởng |

Event và trường dữ liệu dùng ở đây được đặc tả trong [danh sách event E1](chi_so.md#danh-sách-event). Đây là yêu cầu đo cho pilot, chưa phải bằng chứng đã triển khai logging. `refund_ledger_write` chỉ xác nhận ghi sổ; `refund_settlement_updated` mới phản ánh xác nhận tiền về từ ngân hàng/ví. Thiếu xác nhận ghi có là trạng thái cần kiểm tra, chưa đủ để kết luận khách thực tế chưa nhận tiền.
