from django import forms
from .models import SinhVien


class SinhVienForm(forms.ModelForm):
    """Form thêm/sửa sinh viên - tự tạo field từ model"""
    class Meta:
        model = SinhVien
        fields = ['ma_sv', 'ho_ten', 'ngay_sinh', 'lop', 'email', 'so_dt', 'diem_tb']
        widgets = {
            'ngay_sinh': forms.DateInput(attrs={'type': 'date'}),
        }
