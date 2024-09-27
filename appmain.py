import streamlit as st
import streamlit.components.v1 as components

# 定義 HTML 和 JavaScript 代碼
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Camera</title>
</head>
<body>
    <h2>Mobile Camera Stream</h2>
    <video id="video" width="100%" autoplay></video>
    <script>
        const video = document.getElementById('video');

        // 訪問使用者的攝像頭
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                video.srcObject = stream;
            })
            .catch(err => {
                console.error('Error accessing the camera: ', err);
            });
    </script>
</body>
</html>
"""

# 使用 Streamlit 嵌入 HTML 代碼
components.html(html_code, height=400)
