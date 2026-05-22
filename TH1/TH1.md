1. Tạo mảng A chứa 150 số nguyên sinh ra ngẫu nhiên
2. Tạo 5 luồng cùng thực hiện tìm phần tử lớn nhất
3. Các luồng thực hiện nhiệm vụ trên các đoạn riêng rẽ, không giao nhau của A. Trong quá trình thực hiện nhiệm vụ của từng luồng, mỗi khi tùm được một kết quả đúng, luồng sẽ in ra màn hình theo cú pháp: "Tx: <01 kết quả tìm được› : <Thời điểm tìm được kết quả đó›"
4. Sau khi k luồng thực hiện xong, lưồng chính sẽ tổng hợp kết quả cuối cùng và in kết quả này ra màn hình