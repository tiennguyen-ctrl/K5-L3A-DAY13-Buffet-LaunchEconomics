# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Buffet · L3A
- Nhóm được chấm: ALOALO · L3A, theo repo người dùng cung cấp.
- Repo: [zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics).
- Phiên bản đánh giá: nhánh `main`, commit [8a485ea44321116593e6e6b62dc33b2c9f41e110](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics/commit/8a485ea44321116593e6e6b62dc33b2c9f41e110), ngày đọc hồ sơ 2026-11-21 (GMT+7).
- Phạm vi: **30 điểm hội đồng C6–C8**, theo `RUBRIC.md`; không chấm thay 70 điểm C1–C5 của trợ giảng.

Đây là **bản chấm đề xuất trên hồ sơ**, có Codex hỗ trợ đọc và kiểm số; Sang và Phương cần đối chiếu trước khi chốt. Chưa ghi nhận trao đổi hay câu trả lời thực tế của ALOALO.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Go có điều kiện, thu hẹp noi_dia + hang_nang; nêu xem lại 100% tốn 0,98–1,03× [simulated], power 0,64 nếu tác động chỉ 5 điểm, hang_nang thành công 74,1%. Có kế hoạch giảm xem lại, chữ ký chấp nhận MDE 6 điểm, sửa ca 7/20 và lùi quyết định nếu chưa đủ 299 yêu cầu/người. Các bất lợi chính đều được nêu cùng cách xử lý. Nguồn: [hồ sơ launch, mục 3, 6 và điều kiện](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics/blob/8a485ea44321116593e6e6b62dc33b2c9f41e110/report/team/ho_so_launch_v0.md). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **5** | Các bảng chi phí, rủi ro và hồ sơ launch đã ghi simulated; phạm vi thu hẹp có lý do, quoc_te tốn 1,88× mức 12.000 đ [simulated]. Tuy nhiên `pilot_plan.yaml` dòng scope dùng 1,88× và 0,85× mà chưa gắn nhãn simulated hoặc liệt kê hai giá trị này trong simulated_inputs, nên chưa đạt yêu cầu nhãn ở mọi số chi phí giả lập. Nguồn: [pilot_plan.yaml, dòng 26 và 52](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics/blob/8a485ea44321116593e6e6b62dc33b2c9f41e110/report/team/pilot_plan.yaml#L26). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **5** | Có ngẫu nhiên theo staff và đối chứng đồng thời; kế hoạch 20 cụm/nhóm × 299 yêu cầu, DE 6,96 cho 859,20 yêu cầu hiệu dụng, đủ mục tiêu 859 ở MDE 6 điểm. Nhưng luật mở lại >5% “TRONG 7 ngày đầu” chưa bảo đảm đủ 7 ngày theo dõi sau đóng, cũng chưa quy định giám sát phần còn lại của pilot; luật chi phí thiếu hạn thực hiện hành động. Nguồn: [pilot_plan.yaml, các luật dừng](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics/blob/8a485ea44321116593e6e6b62dc33b2c9f41e110/report/team/pilot_plan.yaml#L45). |
| **Tổng** | | | | **20 / 30** | Điểm đề xuất trên phiên bản hồ sơ đã ghim ở trên. |

**Quyết định đề xuất của hội đồng:** Go có điều kiện.

**Lý do:** Hướng pilot thu hẹp phù hợp bằng chứng kinh tế và nhóm đã nêu các số bất lợi. Trước khi bắt đầu cần bổ sung nhãn simulated còn thiếu, sửa cách đo và lịch giám sát luật mở lại, ghi rõ hạn hành động của luật chi phí. Chỉ kết luận hiệu quả khi cả hai nhánh đạt cỡ mẫu đã định và các yêu cầu đã đủ cửa sổ theo dõi 7 ngày; nếu chưa đủ thì lùi ngày quyết định.

**Một câu hỏi cho đội trình:** Luật dừng dùng tỉ lệ mở lại 7 ngày >5% ngay trong 7 ngày đầu. Với yêu cầu vừa đóng vào cuối tuần đầu, nhóm chọn cohort và mẫu số thế nào để không coi dữ liệu chưa đủ theo dõi là không mở lại, và ngày quyết định sẽ lùi ra sao nếu cần chờ đủ cửa sổ 7 ngày?

**Câu trả lời của đội trình (ghi lại tại buổi):** (chưa có; ghi lại nguyên văn câu trả lời thực tế của ALOALO tại buổi duyệt chéo 17:25)

## Các điểm cần sửa và kiểm số bổ sung

1. **Nhãn giả lập:** thêm simulated cho các tỉ số chi phí 1,88×, 0,85× trong scope, hoặc liệt kê rõ là chi phí tính từ các phút `_simulated` trong simulated_inputs. Không trừ điểm vì ba chỉ số 82,83%, 27,12%, 4,25% không gắn simulated: chúng được tính từ các cột kết quả, không phải cột phút `_simulated`, như nhóm giải thích trong [chi_so.md](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics/blob/8a485ea44321116593e6e6b62dc33b2c9f41e110/report/team/chi_so.md#L3).
2. **Luật dừng:** dùng cohort đủ theo dõi 7 ngày sau đóng và quy định lịch giám sát suốt pilot; chưa đủ dữ liệu thì ghi chưa đủ dữ liệu và chưa tăng rollout. Bổ sung hạn xử lý luật chi phí và cách dừng ngay khi đối soát phát hiện hoàn trùng hoặc báo thành công sai. Phần điều kiện đã có đối soát mỗi giờ, nhưng các tình huống này chưa thành luật dừng riêng trong YAML.
3. **Phân biệt phạm vi chi phí:** [đoạn đề xuất trong hồ sơ launch](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics/blob/8a485ea44321116593e6e6b62dc33b2c9f41e110/report/team/ho_so_launch_v0.md#L17) gán 0,49× cho phạm vi pilot, trong khi [A2](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics/blob/8a485ea44321116593e6e6b62dc33b2c9f41e110/report/team/bang_chi_phi.md#L27) xác định đó là toàn bộ 1.200 yêu cầu. Tính kiểm riêng noi_dia + hang_nang: (3.072.513,274 + 82 × 12.000) ÷ 982 ≈ **4.131 đ/yêu cầu = 0,34× [simulated]**, chưa cộng cố định; không so lẫn với chi phí trên mỗi việc thành công. Đây là lỗi gán phạm vi cần sửa; bản chấm vẫn giữ C6 ở 10 vì sửa phạm vi không đảo chiều đề xuất và các bất lợi chính đã được nêu, xử lý.

**Cách kiểm số:** đọc hai CSV tại commit đã ghim, cộng token vào ×26/1.000 + token ra ×130/1.000 + tool ×15 + phút xem lại/làm lại `_simulated` ×2.000; cộng 12.000 đ cho mỗi yêu cầu không thành công rồi chia tổng yêu cầu. Kết quả toàn mẫu: 978/1.200 việc thành công, tổng 4.373.585,132 đ và 5.864,654 đ/yêu cầu [simulated]; phạm vi pilot: 900/982 việc thành công, tổng 3.072.513,274 đ và 39/982 mở lại. Công thức cỡ mẫu cho 0,70 so với 0,76 cho 859 yêu cầu hiệu dụng; 20 × 299 ÷ [1 + 298 × 0,02] = 859,20. Đối chiếu với [mã tính](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics/blob/8a485ea44321116593e6e6b62dc33b2c9f41e110/src/lab13.py), [CSV lượt chạy](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics/blob/8a485ea44321116593e6e6b62dc33b2c9f41e110/src/logix_runs.csv) và [CSV yêu cầu](https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics/blob/8a485ea44321116593e6e6b62dc33b2c9f41e110/src/logix_requests.csv). Chỉ kiểm số phục vụ C6–C8, không suy ra điểm tổng 100.
