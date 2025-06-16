import pymysql

# Kết nối tới MySQL
connection = pymysql.connect(
    host='my_mysql',          # localhost (host máy bạn)
    port=3306,                 # cổng expose từ docker-compose
    user='user_cv',            # user bạn khai báo trong compose
    password='userpass123',    # mật khẩu user đó
    database='cv',             # database mặc định tạo sẵn
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Ví dụ tạo bảng
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                position VARCHAR(100)
            )
        """)
        connection.commit()

        # Ví dụ chèn dữ liệu
        cursor.execute("INSERT INTO employees (name, position) VALUES (%s, %s)", ("Nguyen Van A", "Developer"))
        connection.commit()

        # Ví dụ truy vấn
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
finally:
    connection.close()
