from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import SinhVien
from .forms import SinhVienForm


def index(request):
    """Trang chủ - danh sách sinh viên"""
    q = request.GET.get('q', '').strip()
    if q:
        sinh_vien_list = SinhVien.objects.filter(
            Q(ho_ten__icontains=q) | Q(ma_sv__icontains=q) |
            Q(lop__icontains=q) | Q(email__icontains=q)
        )
    else:
        sinh_vien_list = SinhVien.objects.all()
    return render(request, 'home/index.html', {
        'sinh_vien_list': sinh_vien_list,
        'search_query': q
    })


def them_sinh_vien(request):
    """Thêm sinh viên mới"""
    if request.method == 'POST':
        form = SinhVienForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm sinh viên thành công!')
            return redirect('home:index')
        messages.error(request, 'Vui lòng kiểm tra lại thông tin.')
    else:
        form = SinhVienForm()
    return render(request, 'home/form_sinhvien.html', {'form': form, 'title': 'Thêm sinh viên'})


def sua_sinh_vien(request, pk):
    """Sửa thông tin sinh viên"""
    sv = get_object_or_404(SinhVien, pk=pk)
    if request.method == 'POST':
        form = SinhVienForm(request.POST, instance=sv)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cập nhật thành công!')
            return redirect('home:index')
    else:
        form = SinhVienForm(instance=sv)
    return render(request, 'home/form_sinhvien.html', {'form': form, 'title': 'Sửa sinh viên'})


def xoa_sinh_vien(request, pk):
    """Xóa sinh viên"""
    sv = get_object_or_404(SinhVien, pk=pk)
    if request.method == 'POST':
        sv.delete()
        messages.success(request, 'Đã xóa sinh viên!')
        return redirect('home:index')
    return redirect('home:index')
