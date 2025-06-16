# Sử dụng Ubuntu 22.04 LTS làm base image
FROM ubuntu:22.04

# Cập nhật và cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    vim \
    python3.10-venv \
    python3 \
    python3-pip \
    nodejs \
    npm \
    bash \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Tạo thư mục làm việc
WORKDIR /app

# Sao chép mã nguồn vào container
COPY . /app

# Cài đặt các phụ thuộc (nếu có)
RUN pip3 install -r requirements.txt || true
RUN npm install || true

# Mở cổng 8080 (nếu cần)
EXPOSE 8080

# Chạy lệnh mặc định khi container khởi động
CMD ["bash"]

