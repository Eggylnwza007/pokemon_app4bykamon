นี้เป็นการส่งงานสอบสหกิจ ของ นาย กมล จันบุตรดี (CS) รหัส 643450063-8 กระผมได้ลงมือทำ ข้อที่ 4 เกี่ยวกับ การสร้าง web app ที่ใช้สำหรับ แสดง ข้อมูล POkemon List ผ่านการดึง API จะจากเว็บโดยตรง ของ Pokemon ที่ เปิดให้ทดลองใช้ โดย web จะแสดง ข้อมูล ขนาด ความสูง
และ น้ำหนัก สุดท้าย คือ ธาตุ โดยผมได้เพิ่ม ข้อมูลลายละเอียด เข้าไปเพิ่ม เกี่ยวกับ การ อธิบาย ว่า Pokemon ทำมีพฤติกรรม อะไรบ้างเข้าไป  ซึง การมีตบแต่งเว็บของผมนั้น มีการใช้เครื่องมือ อย่าง Boosterap และ อื่นๆ มีการ เพิ่ม รูปภาพธาตุๆ อีกด้วย 
ขอให้สนุกสำหรับการใช้งาน web นะครับ


Python:

    ใช้สำหรับเขียนโปรแกรมฝั่งเซิร์ฟเวอร์
    ใช้ Flask เป็นเว็บเฟรมเวิร์กในการสร้างแอปพลิเคชัน

HTML:

    ใช้สำหรับสร้างโครงสร้างของหน้าเว็บ
    ไฟล์ HTML ประกอบไปด้วย index.html และ pokemon_detail.html

CSS:

    ใช้สำหรับตกแต่งหน้าเว็บให้สวยงาม
    ไฟล์ CSS ชื่อ style.css

JavaScript:

    ใช้สำหรับทำงานทางฝั่งไคลเอนต์
    ในโปรแกรมนี้ ใช้ไลบรารีจาก Bootstrap และ jQuery ที่ช่วยในการสร้าง UI และการโต้ตอบของผู้ใช้

Bootstrap:

    ใช้สำหรับการออกแบบหน้าเว็บให้สวยงามและเป็น Responsive
    ใช้ CDN สำหรับการโหลด Bootstrap

my_project_folder/
|-- app.py                    # Flask application written in Python
|-- templates/
|   |-- index.html            # HTML template for the main page
|   |-- pokemon_detail.html   # HTML template for the Pokemon detail page
|-- static/
    |-- images/
    |   |-- background.jpg    # Background image
    |-- icons/                # Folder to store type icons
    |   |-- fire.png
    |   |-- water.png
    |   |-- grass.png
    |   |-- ...               # Other type icons
    |-- style.css             # CSS file for styling

คำอธิบายไฟล์แต่ละไฟล์

    app.py: ไฟล์นี้เป็นแอปพลิเคชัน Flask เขียนด้วยภาษา Python ซึ่งรับผิดชอบการดึงข้อมูลจาก PokeAPI และแสดงผลไปยังหน้าเว็บ
    index.html: ไฟล์นี้เป็นเทมเพลต HTML สำหรับหน้าแรกที่แสดงรายชื่อโปเกมอน
    pokemon_detail.html: ไฟล์นี้เป็นเทมเพลต HTML สำหรับหน้ารายละเอียดของโปเกมอนแต่ละตัว
    style.css: ไฟล์นี้เป็น CSS สำหรับการตกแต่งหน้าเว็บ
    images/background.jpg: ไฟล์ภาพพื้นหลังที่ใช้ในหน้าเว็บ
    icons/: โฟลเดอร์ที่เก็บไอคอนของแต่ละธาตุโปเกมอน

ตัวอย่างการใช้งาน

    Python และ Flask:
        รันเซิร์ฟเวอร์ Flask โดยใช้คำสั่ง flask run

    HTML, CSS และ JavaScript:
        ไฟล์ HTML ถูกเรนเดอร์โดย Flask และส่งไปยังเบราว์เซอร์ของผู้ใช้
        CSS ถูกโหลดเพื่อทำให้หน้าเว็บดูสวยงามและเป็นระเบียบ
        JavaScript (Bootstrap และ jQuery) ถูกใช้เพื่อเพิ่มความสามารถในการโต้ตอบ

