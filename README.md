# Hệ thống Quản lý Thư viện - DTC245200167

Báo cáo thực hành học phần **Triển khai và Quản trị Hệ thống phần mềm**.

## Thông tin sinh viên
- **Họ và tên:** Nguyễn Bế Hiệp
- **Mã sinh viên:** DTC245200167
- **Lớp:** CNTT 23H
- **Giảng viên hướng dẫn:** ThS. Lê Khánh Dương

## Kiến trúc Hệ thống (9 Container Services)
1. **Nginx:** Reverse Proxy & Security Headers (Port 80)
2. **Backend App:** FastAPI Web Application (Port 8000)
3. **Database:** PostgreSQL 15 & pgAdmin4 (Port 5050)
4. **Monitoring:** Prometheus (Port 9090) & cAdvisor
5. **Visualization:** Grafana Dashboard (Port 3000)
6. **Centralized Logging:** Loki (Port 3100) & Promtail

## Hướng dẫn Khởi chạy
```bash
git clone [https://github.com/nguyenbehiep03032006/QT-TKHT-QuanLyThuVien-DTC245200167.git](https://github.com/nguyenbehiep03032006/QT-TKHT-QuanLyThuVien-DTC245200167.git)
cd QT-TKHT-QuanLyThuVien-DTC245200167
sudo docker compose up -d
