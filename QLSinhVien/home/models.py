from django.db import models


class SinhVien(models.Model):
    """Model sinh viên - mỗi field = 1 cột trong bảng database"""
    ma_sv = models.CharField('Mã sinh viên', max_length=20, unique=True)
    ho_ten = models.CharField('Họ tên', max_length=100)
    ngay_sinh = models.DateField('Ngày sinh', null=True, blank=True)
    lop = models.CharField('Lớp', max_length=20, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    so_dt = models.CharField('Số điện thoại', max_length=15, blank=True, null=True)
    diem_tb = models.FloatField('Điểm TB', null=True, blank=True)
    ngay_tao = models.DateTimeField('Ngày tạo', auto_now_add=True)

    class Meta:
        verbose_name = 'Sinh viên'
        verbose_name_plural = 'Sinh viên'
        ordering = ['-ngay_tao']

    def __str__(self):
        return f'{self.ma_sv} - {self.ho_ten}'
