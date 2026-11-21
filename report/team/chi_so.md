# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | Trong các yêu cầu có `duoc_xem_lai` bằng 1, lấy tỉ lệ có `quyet_dinh_xem_lai` là `sua` hoặc `bo` | **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200) |
| Dùng | Tỉ lệ yêu cầu đủ điều kiện mà nhân viên mở trợ lý | Số yêu cầu đủ điều kiện thuộc nhóm can thiệp có ít nhất một lượt mở trợ lý do nhân viên thực hiện ÷ tổng số yêu cầu đủ điều kiện thuộc nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ khoản hoàn sai số tiền trong mẫu kiểm tra hằng tuần | Số khoản hoàn đã kiểm tra có số tiền thực tế khác số tiền đúng theo chính sách áp dụng ÷ tổng số khoản hoàn đã kiểm tra trong mẫu | Không cần tính |

Các chỉ số trên mô tả đợt chạy thử giả lập, vốn không có nhóm đối chứng. Nguồn tính là `logix_requests.csv`, qua `tinh_chi_so_e1` trong `src/lab13.py`.

## Danh sách event

Đây là đặc tả event cần triển khai cho pilot; hai file CSV hiện có không chứng minh các event này đã được ghi. Hệ thống cấp một `trace_id` chung cho mỗi yêu cầu, kể cả yêu cầu thuộc nhóm đối chứng. Mọi event mang `event_id`, `trace_id` và `request_id`; `event_id` dùng khử bản ghi gửi lại. Mỗi lần chạy agent mang thêm `run_trace_id`. Thời gian lưu theo UTC và đổi sang `customer_timezone` khi kiểm tra giờ gửi. `order_id` + `entitlement_id` xác định cùng một quyền lợi hoàn tiền xuyên suốt các yêu cầu gửi lại.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận | `trace_id`, `request_id`, `created_at`, `loai`, `depot`, `pilot_eligible`, `arm` | Khi tiếp nhận và ghi nhận phân nhóm |
| `customer_message_received` | Kênh tiếp nhận | `trace_id`, `request_id`, `message_id`, `input_type` (text/audio/image), `received_at` | Mỗi lần nhận tin nhắn của khách, kể cả tin nhắn tiếp theo trong cùng yêu cầu |
| `assistant_input_rejected` | Agent | `trace_id`, `request_id`, `message_id`, `input_type`, `reason` (unsupported_input), `recovery_options`, `rejected_at` | Khi từ chối một dạng đầu vào và đưa hướng tiếp tục |
| `assistant_opened` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `opened_at` | Khi nhân viên chủ động mở trợ lý cho yêu cầu |
| `agent_run_completed` | Agent | `trace_id`, `request_id`, `run_trace_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `completed_at` | Sau mỗi lần chạy, kể cả lần lỗi |
| `staff_review_decision` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `decision` (giu/sua/bo), `reviewed_at`, `phut_xem_lai` | Khi nhân viên chốt quyết định cho yêu cầu đã xem lại |
| `staff_rework_completed` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `reason`, `phut_lam_lai`, `completed_at` | Khi nhân viên làm lại xong |
| `handoff_to_staff` | Agent | `trace_id`, `request_id`, `reason`, `handoff_at` | Khi chuyển yêu cầu cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | `trace_id`, `request_id`, `order_id`, `entitlement_id`, `refund_id`, `idempotency_key`, `amount_vnd`, `status` (success/failed/pending), `recorded_at` | Khi sổ cái trả kết quả ghi khoản hoàn; success chưa chứng minh khách đã nhận tiền |
| `refund_settlement_updated` | Dịch vụ thanh toán | `trace_id`, `request_id`, `refund_id`, `provider_transaction_id`, `provider_event_id`, `destination_type` (bank/wallet), `status` (pending/credited/failed), `credited_at`, `received_at` | Khi nhận cập nhật từ ngân hàng/ví; chỉ đặt credited khi có xác nhận ghi có của bên nhận |
| `notification_sent` | Dịch vụ thông báo | `trace_id`, `request_id`, `notification_id`, `channel`, `urgency` (normal/urgent), `customer_timezone`, `overnight_opt_in`, `sent_at`, `provider_message_id` | Khi nhà cung cấp xác nhận đã nhận lệnh gửi thành công; lưu tùy chọn khách tại thời điểm gửi, chưa khẳng định đã đọc |
| `ticket_closed` | Hệ thống ticket | `trace_id`, `request_id`, `refund_id` (nếu có), `closed_by` (customer/staff/system), `close_reason`, `closed_at` | Mỗi lần yêu cầu được đóng; close_reason=refund_received khi khách xác nhận đã nhận tiền |
| `ticket_reopened` | Hệ thống ticket | `trace_id`, `request_id`, `reopened_at`, `reason` | Mỗi lần yêu cầu được mở lại |
| `audit_sample_checked` | Kế toán | `trace_id`, `request_id`, `refund_id`, `audit_batch_id`, `actual_amount_vnd`, `expected_amount_vnd`, `policy_version`, `checked_at` | Khi kiểm tra xong một khoản hoàn trong mẫu tuần |

**Kiểm tra chéo**

| Chỉ số | Event và cách tính |
| --- | --- |
| Đóng trong 24 giờ và không mở lại trong 7 ngày | Lấy các yêu cầu từ `refund_request_created`. Dùng lần `ticket_closed` đầu tiên để kiểm tra mốc 24 giờ, rồi tìm `ticket_reopened` trong 7 ngày kể từ lần đóng đó. Chia số yêu cầu đạt cả hai điều kiện cho tổng số yêu cầu trong tập đánh giá. |
| Bỏ qua gợi ý | Từ `staff_review_decision`, giữ quyết định cuối của mỗi yêu cầu đã xem lại. Chia số quyết định `sua` hoặc `bo` cho tổng số quyết định `giu`, `sua` hoặc `bo`. |
| Mở lại trong 7 ngày | Nối `ticket_closed` và `ticket_reopened`. Đếm một lần mỗi yêu cầu có lượt mở lại trong 7 ngày sau một lần đóng, rồi chia cho tổng số yêu cầu trong tập đánh giá từ `refund_request_created`. |
| Nhân viên mở trợ lý | Lọc `refund_request_created` theo `pilot_eligible` và nhóm can thiệp trong kỳ đo. Chia số yêu cầu trong tập này có ít nhất một `assistant_opened` cho tổng số yêu cầu trong tập. |
| Hoàn sai số tiền | Từ `audit_sample_checked`, đếm các `refund_id` duy nhất trong mẫu tuần. Chia số khoản có `actual_amount_vnd` khác `expected_amount_vnd` cho tổng số khoản đã kiểm tra. |

Khi tính hai chỉ số có cửa sổ 7 ngày, chốt cohort theo cùng kỳ tiếp nhận của hai nhánh và đợi đủ 7 ngày theo dõi sau đóng cho các yêu cầu đã đóng trong cohort. Giữ yêu cầu chưa đóng trong mẫu số tổng yêu cầu và báo riêng số lượng; không coi yêu cầu chưa đủ theo dõi là không mở lại. Tính riêng theo nhánh can thiệp và đối chứng; mẫu số bằng 0 hoặc dữ liệu chưa đủ thì ghi "chưa đủ dữ liệu", không ghi 0%.

**Đối chiếu với bảng lỗi C**

| Ca | Event và khóa nối | Cách kiểm tra |
| --- | --- | --- |
| 14 | `ticket_closed` + `refund_settlement_updated`, nối bằng `refund_id` | Với xác nhận nhận tiền của khách, chỉ dùng cập nhật ngân hàng/ví đã nhận trước hoặc tại `closed_at`; nếu chưa có credited thì cảnh báo cần xác minh. Khử cập nhật nhà cung cấp bị gửi lại bằng `provider_event_id`. |
| 20 | `refund_ledger_write`, nhóm theo `order_id` + `entitlement_id` | Đếm các `refund_id` khác nhau có success; hơn một là nghi hoàn trùng. Không dùng riêng `request_id` vì khách gửi lại có thể tạo yêu cầu mới. |
| 16 | `notification_sent` | Đổi `sent_at` sang `customer_timezone` rồi kiểm tra giờ yên lặng, mức khẩn cấp và tùy chọn nhận ban đêm. Thiếu múi giờ hoặc tùy chọn thì báo thiếu dữ liệu để xác minh. |
| 11 | `assistant_input_rejected` + `customer_message_received` + `handoff_to_staff`, nối bằng `request_id` | Với mỗi yêu cầu, lấy lần từ chối unsupported_input đầu tiên trong kỳ. Chỉ tính khi đủ 24 giờ; tìm tin nhắn chữ hoặc lượt chuyển nhân viên trong 24 giờ sau lần từ chối đó; không đồng nhất việc chưa đóng ticket với bỏ cuộc. |
| 05 | `audit_sample_checked`, khóa `audit_batch_id` + `refund_id` | Mỗi khoản tính một lần trong kỳ kiểm tra; số đúng phải dựa trên chính sách và số thực trả sau giảm giá. |

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%: chi phí mỗi việc thành công 4.472 → 6.787 đ [simulated] (B1, yếu tố nhạy nhất) | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 48/982 = 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp phạm vi về noi_dia; rà 20 trace có làm lại để tìm nguyên nhân | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] (B4) | % yêu cầu được xem lại còn > 50% ở cuối bước rollout 0,25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; mục tiêu mỗi lần xem lại ≤ 5 phút (hoà vốn 5,1 phút) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] (A4) | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | Kế toán trưởng |
