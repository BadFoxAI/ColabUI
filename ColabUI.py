from IPython.display import HTML

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colab HTML/CSS/JS Feature Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 20px;
            font-size: 14px;
        }
        h1 {
            color: #333;
            font-size: 24px;
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        th, td {
            border: 1px solid #ddd;
            padding: 15px;
            text-align: left;
        }
        th {
            background-color: #007bff;
            color: white;
            font-size: 16px;
        }
        .working {
            color: green;
        }
        .not-working {
            color: red;
        }
        .demo-section {
            display: none;
            margin-top: 15px;
            padding: 15px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .demo-section video {
            width: 300px;
            height: auto;
        }
        .demo-section canvas, .demo-section svg {
            width: 200px;
            height: 200px;
        }
        .toggle-button {
            background: none;
            border: none;
            cursor: pointer;
            font-size: 18px;
            color: #007bff;
        }
        .toggle-button:focus {
            outline: none;
        }
        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        .css-animation-demo {
            width: 100px;
            height: 100px;
            background-color: orange;
            animation: spin 2s linear infinite;
        }
    </style>
</head>
<body>
    <h1>HTML/CSS/JS Feature Test in Colab</h1>
    <p>Testing various features to see what works in Colab.</p>

    <table>
        <thead>
            <tr>
                <th>Feature</th>
                <th>Status</th>
                <th>Demo</th>
            </tr>
        </thead>
        <tbody>
            <!-- HTML5 Canvas -->
            <tr>
                <td>HTML5 Canvas</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('canvas')">▼</button>
                    <div id="canvas" class="demo-section">
                        <canvas id="myCanvas" width="200" height="200"></canvas>
                        <p>Canvas drawing a circle.</p>
                    </div>
                </td>
            </tr>
            <!-- HTML5 Video -->
            <tr>
                <td>HTML5 Video</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('video')">▼</button>
                    <div id="video" class="demo-section">
                        <video controls width="300">
                            <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
                            Video not supported.
                        </video>
                        <p>Playing a video.</p>
                    </div>
                </td>
            </tr>
            <!-- HTML5 Audio -->
            <tr>
                <td>HTML5 Audio</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('audio')">▼</button>
                    <div id="audio" class="demo-section">
                        <audio controls>
                            <source src="https://www.w3schools.com/html/horse.ogg" type="audio/ogg">
                            Audio not supported.
                        </audio>
                        <p>Playing an audio clip.</p>
                    </div>
                </td>
            </tr>
            <!-- SVG -->
            <tr>
                <td>SVG</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('svg')">▼</button>
                    <div id="svg" class="demo-section">
                        <svg width="200" height="200">
                            <circle cx="100" cy="100" r="80" stroke="black" stroke-width="3" fill="lightblue" />
                        </svg>
                        <p>SVG circle element.</p>
                    </div>
                </td>
            </tr>
            <!-- Details Element -->
            <tr>
                <td>Details Element</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('details')">▼</button>
                    <div id="details" class="demo-section">
                        <details>
                            <summary>Click to expand</summary>
                            <p>This is a details element with more content inside.</p>
                        </details>
                        <p>Collapsible content.</p>
                    </div>
                </td>
            </tr>
            <!-- Progress Element -->
            <tr>
                <td>Progress Element</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('progress')">▼</button>
                    <div id="progress" class="demo-section">
                        <progress value="75" max="100"></progress>
                        <p>Progress bar at 75%.</p>
                    </div>
                </td>
            </tr>
            <!-- Meter Element -->
            <tr>
                <td>Meter Element</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('meter')">▼</button>
                    <div id="meter" class="demo-section">
                        <meter value="0.6"></meter>
                        <p>Meter indicating 60%.</p>
                    </div>
                </td>
            </tr>
            <!-- CSS Grid -->
            <tr>
                <td>CSS Grid</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('css-grid')">▼</button>
                    <div id="css-grid" class="demo-section">
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                            <div style="background: lightblue;">Grid Item 1</div>
                            <div style="background: lightcoral;">Grid Item 2</div>
                            <div style="background: lightgreen;">Grid Item 3</div>
                            <div style="background: lightyellow;">Grid Item 4</div>
                        </div>
                        <p>A simple CSS Grid layout.</p>
                    </div>
                </td>
            </tr>
            <!-- CSS Flexbox -->
            <tr>
                <td>CSS Flexbox</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('css-flexbox')">▼</button>
                    <div id="css-flexbox" class="demo-section">
                        <div id="flex-container" style="display: flex; gap: 10px;">
                            <div style="background: lightgreen; flex: 1;">Flex Item 1</div>
                            <div style="background: lightyellow; flex: 2;">Flex Item 2</div>
                        </div>
                        <button onclick="changeFlexDirection()">Change Flex Direction</button>
                        <button onclick="changeFlexAlign()">Change Alignment</button>
                        <p>A flexible layout with interactive controls.</p>
                    </div>
                </td>
            </tr>
            <!-- CSS Animation -->
            <tr>
                <td>CSS Animation</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('css-animation')">▼</button>
                    <div id="css-animation" class="demo-section">
                        <div class="css-animation-demo"></div>
                        <p>Box rotating indefinitely.</p>
                    </div>
                </td>
            </tr>
            <!-- JavaScript Notification -->
            <tr>
                <td>JavaScript Notification</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('js-notification')">▼</button>
                    <div id="js-notification" class="demo-section">
                        <button onclick="showNotification()">Show Notification</button>
                        <p>Click the button to see a subtle notification.</p>
                    </div>
                </td>
            </tr>
            <!-- LocalStorage -->
            <tr>
                <td>LocalStorage</td>
                <td class="working">✔️ Working</td>
                <td>
                    <button class="toggle-button" onclick="toggleDemo('local-storage')">▼</button>
                    <div id="local-storage" class="demo-section">
                        <button onclick="saveToLocalStorage()">Save Data</button>
                        <button onclick="readFromLocalStorage()">Read Data</button>
                        <p>Save and read data from LocalStorage.</p>
                    </div>
                </td>
            </tr>
            <!-- Geolocation -->
            <tr>
                <td>Geolocation</td>
                <td class="not-working">❌ Not Working: Geolocation not supported in Colab.</td>
                <td>No demo available.</td>
            </tr>
        </tbody>
    </table>

    <script>
        function toggleDemo(sectionId) {
            var demo = document.getElementById(sectionId);
            var button = demo.previousElementSibling;
            if (demo.style.display === "block") {
                demo.style.display = "none";
                button.textContent = "▼";
            } else {
                demo.style.display = "block";
                button.textContent = "▲";
            }
        }

        function showNotification() {
            var notification = document.createElement('div');
            notification.style.position = 'fixed';
            notification.style.bottom = '10px';
            notification.style.right = '10px';
            notification.style.backgroundColor = 'green';
            notification.style.color = 'white';
            notification.style.padding = '10px';
            notification.style.borderRadius = '5px';
            notification.textContent = 'Notification: JavaScript is working!';
            document.body.appendChild(notification);
            setTimeout(function() {
                notification.style.opacity = '0';
                setTimeout(function() {
                    document.body.removeChild(notification);
                }, 500);
            }, 2000);
        }

        function saveToLocalStorage() {
            localStorage.setItem('testKey', 'testValue');
            showNotification();
        }

        function readFromLocalStorage() {
            var data = localStorage.getItem('testKey');
            var notification = document.createElement('div');
            notification.style.position = 'fixed';
            notification.style.bottom = '10px';
            notification.style.right = '10px';
            notification.style.backgroundColor = 'blue';
            notification.style.color = 'white';
            notification.style.padding = '10px';
            notification.style.borderRadius = '5px';
            notification.textContent = 'Data from LocalStorage: ' + data;
            document.body.appendChild(notification);
            setTimeout(function() {
                notification.style.opacity = '0';
                setTimeout(function() {
                    document.body.removeChild(notification);
                }, 500);
            }, 2000);
        }

        // Canvas drawing script
        const ctx = document.getElementById('myCanvas').getContext('2d');
        ctx.beginPath();
        ctx.arc(100, 100, 80, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fillStyle = 'lightblue';
        ctx.fill();

        // Enhanced Flexbox demo scripts
        let flexDirection = 'row';
        let flexAlign = 'stretch';

        function changeFlexDirection() {
            const container = document.getElementById('flex-container');
            if (flexDirection === 'row') {
                container.style.flexDirection = 'column';
                flexDirection = 'column';
            } else {
                container.style.flexDirection = 'row';
                flexDirection = 'row';
            }
        }

        function changeFlexAlign() {
            const container = document.getElementById('flex-container');
            if (flexAlign === 'stretch') {
                container.style.alignItems = 'center';
                flexAlign = 'center';
            } else {
                container.style.alignItems = 'stretch';
                flexAlign = 'stretch';
            }
        }
    </script>
</body>
</html>
"""

# Render the HTML in Colab
HTML(html_content)
