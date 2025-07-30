# CV Portfolio Website

Một website CV hiện đại được xây dựng bằng Django để showcase kỹ năng và dự án lập trình.

## 🌟 Tính năng

- **Responsive Design**: Tối ưu cho mọi thiết bị
- **Admin Panel**: Quản lý nội dung dễ dàng
- **Portfolio Showcase**: Hiển thị dự án với hình ảnh và video
- **Contact Form**: Form liên hệ với AJAX
- **Modern UI**: Giao diện hiện đại với animations
- **Media Support**: Hỗ trợ upload và hiển thị ảnh/video

## 🛠 Công nghệ sử dụng

- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5, AOS Animation Library
- **Database**: SQLite (có thể chuyển sang PostgreSQL)
- **Styling**: Custom CSS với CSS Grid và Flexbox
- **JavaScript**: Vanilla JS với modern ES6+

## 📁 Cấu trúc project

```
cv_project/
├── cv_project/          # Main project settings
├── portfolio/           # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── admin.py        # Admin configuration
│   ├── forms.py        # Forms
│   └── urls.py         # URL patterns
├── templates/          # HTML templates
├── static/            # CSS, JS, images
├── media/             # User uploaded files
└── manage.py          # Django management script
```

## 🚀 Cài đặt và chạy

1. **Clone repository**
```bash
git clone https://github.com/phamnhatthi/CV_Profile.git
cd CV_Profile
```

2. **Tạo virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

3. **Cài đặt dependencies**
```bash
pip install django pillow django-crispy-forms crispy-bootstrap5
```

4. **Chạy migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Tạo superuser**
```bash
python manage.py createsuperuser
```

6. **Chạy development server**
```bash
python manage.py runserver
```

7. **Truy cập website**
- Website: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin

## 📝 Sử dụng

1. **Đăng nhập Admin Panel** để thêm:
   - Thông tin cá nhân (Profile)
   - Kỹ năng (Skills)
   - Kinh nghiệm làm việc (Experience)
   - Học vấn (Education)
   - Dự án (Projects)

2. **Upload media files**:
   - Ảnh đại diện
   - Ảnh dự án
   - Video demo

3. **Tùy chỉnh nội dung** và share link với nhà tuyển dụng!

## 🎨 Screenshots

### Trang chủ
- Hero section với thông tin cá nhân
- Kỹ năng với progress bar animations
- Dự án nổi bật
- Timeline kinh nghiệm và học vấn

### Trang dự án
- Grid layout responsive
- Filter theo loại dự án
- Phân trang
- Chi tiết dự án với video demo

### Trang liên hệ
- Form liên hệ với validation
- Thông tin liên hệ
- Social media links

## 🔧 Customization

### Thay đổi màu sắc
Sửa file `static/css/style.css`, phần CSS variables:

```css
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --warning-color: #ffc107;
    /* ... */
}
```

### Thêm sections mới
1. Tạo model trong `portfolio/models.py`
2. Thêm vào admin trong `portfolio/admin.py`
3. Cập nhật view và template

## 📱 Responsive Design

- **Mobile First**: Thiết kế tối ưu cho mobile trước
- **Breakpoints**: 
  - Mobile: < 768px
  - Tablet: 768px - 992px
  - Desktop: > 992px

## 🌐 Deployment

### Heroku
1. Cài đặt `gunicorn` và `whitenoise`
2. Tạo `Procfile`
3. Cấu hình `settings.py` cho production
4. Deploy lên Heroku

### VPS/Cloud
1. Cài đặt Nginx và uWSGI/Gunicorn
2. Cấu hình reverse proxy
3. Setup SSL certificate
4. Configure static files serving

## 🤝 Contributing

1. Fork repository
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

**Phạm Nhật Thi**
- Email: nhatthiph@gmail.com
- GitHub: [@phamnhatthi](https://github.com/phamnhatthi)
- Website: [Your Website]

---

⭐ Star this repository if you find it helpful!
