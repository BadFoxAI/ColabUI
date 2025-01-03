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
        }
        h1 {
            color: #333;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #007bff;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .working {
            color: green;
        }
        .not-working {
            color: red;
        }
        .demo {
            margin-top: 10px;
            padding: 10px;
            background: white;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <h1>HTML/CSS/JS Feature Test in Colab</h1>
    <p>Testing various features to see what works in Colab.</p>

    <!-- Feature Test Section -->
    <div id="feature-test">
        <h2>Test Results</h2>
        <table>
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>Status</th>
                    <th>Demo</th>
                </tr>
            </thead>
            <tbody id="results">
                <!-- Results will be populated by JavaScript -->
            </tbody>
        </table>
    </div>

    <!-- Test Elements -->
    <div id="test-elements" style="display: none;">
        <!-- HTML5 Elements -->
        <canvas id="test-canvas" width="200" height="100"></canvas>
        <video id="test-video" controls width="200">
            <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <audio id="test-audio" controls>
            <source src="https://www.w3schools.com/html/horse.ogg" type="audio/ogg">
            Your browser does not support the audio element.
        </audio>
        <svg id="test-svg" width="100" height="100">
            <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
        </svg>
        <details id="test-details">
            <summary>Click to expand</summary>
            <p>This is a details element.</p>
        </details>
        <progress id="test-progress" value="50" max="100"></progress>
        <meter id="test-meter" value="0.6"></meter>

        <!-- CSS Features -->
        <div id="test-css-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <div style="background: lightblue;">Grid Item 1</div>
            <div style="background: lightcoral;">Grid Item 2</div>
        </div>
        <div id="test-css-flexbox" style="display: flex; gap: 10px;">
            <div style="background: lightgreen;">Flex Item 1</div>
            <div style="background: lightyellow;">Flex Item 2</div>
        </div>
        <div id="test-css-animation" style="width: 100px; height: 100px; background: orange; animation: spin 2s linear infinite;"></div>
        <style>
            @keyframes spin {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
        </style>

        <!-- JavaScript Features -->
        <button id="test-button" onclick="alert('Button clicked!')">Click Me</button>
        <input id="test-input" type="text" placeholder="Type something...">
        <div id="test-localstorage"></div>
        <div id="test-geolocation"></div>
    </div>

    <script>
        // Function to test features
        function testFeature(feature, testFn, demoFn) {
            try {
                const result = testFn();
                const demo = demoFn ? demoFn() : null;
                return { working: true, message: result, demo };
            } catch (error) {
                return { working: false, message: error.message, demo: null };
            }
        }

        // Test Results
        const results = [
            {
                feature: "HTML5 Canvas",
                test: () => {
                    const canvas = document.getElementById("test-canvas");
                    const ctx = canvas.getContext("2d");
                    ctx.fillStyle = "lightblue";
                    ctx.fillRect(10, 10, 180, 80);
                    return "Canvas drawn.";
                },
                demo: () => `<div class="demo"><canvas id="test-canvas" width="200" height="100"></canvas></div>`
            },
            {
                feature: "HTML5 Video",
                test: () => {
                    const video = document.getElementById("test-video");
                    return video.canPlayType("video/mp4") ? "Video supported." : "Video not supported.";
                },
                demo: () => `<div class="demo"><video id="test-video" controls width="200">
                    <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video></div>`
            },
            {
                feature: "HTML5 Audio",
                test: () => {
                    const audio = document.getElementById("test-audio");
                    return audio.canPlayType("audio/ogg") ? "Audio supported." : "Audio not supported.";
                },
                demo: () => `<div class="demo"><audio id="test-audio" controls>
                    <source src="https://www.w3schools.com/html/horse.ogg" type="audio/ogg">
                    Your browser does not support the audio element.
                </audio></div>`
            },
            {
                feature: "SVG",
                test: () => {
                    const svg = document.getElementById("test-svg");
                    return svg.querySelector("circle") ? "SVG rendered." : "SVG not rendered.";
                },
                demo: () => `<div class="demo"><svg id="test-svg" width="100" height="100">
                    <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
                </svg></div>`
            },
            {
                feature: "Details Element",
                test: () => {
                    const details = document.getElementById("test-details");
                    return details.open ? "Details expanded." : "Details collapsed.";
                },
                demo: () => `<div class="demo"><details id="test-details">
                    <summary>Click to expand</summary>
                    <p>This is a details element.</p>
                </details></div>`
            },
            {
                feature: "Progress Element",
                test: () => {
                    const progress = document.getElementById("test-progress");
                    return progress.value ? "Progress displayed." : "Progress not displayed.";
                },
                demo: () => `<div class="demo"><progress id="test-progress" value="50" max="100"></progress></div>`
            },
            {
                feature: "Meter Element",
                test: () => {
                    const meter = document.getElementById("test-meter");
                    return meter.value ? "Meter displayed." : "Meter not displayed.";
                },
                demo: () => `<div class="demo"><meter id="test-meter" value="0.6"></meter></div>`
            },
            {
                feature: "CSS Grid",
                test: () => {
                    const grid = document.getElementById("test-css-grid");
                    return grid.style.display === "grid" ? "Grid displayed." : "Grid not displayed.";
                },
                demo: () => `<div class="demo"><div id="test-css-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                    <div style="background: lightblue;">Grid Item 1</div>
                    <div style="background: lightcoral;">Grid Item 2</div>
                </div></div>`
            },
            {
                feature: "CSS Flexbox",
                test: () => {
                    const flexbox = document.getElementById("test-css-flexbox");
                    return flexbox.style.display === "flex" ? "Flexbox displayed." : "Flexbox not displayed.";
                },
                demo: () => `<div class="demo"><div id="test-css-flexbox" style="display: flex; gap: 10px;">
                    <div style="background: lightgreen;">Flex Item 1</div>
                    <div style="background: lightyellow;">Flex Item 2</div>
                </div></div>`
            },
            {
                feature: "CSS Animation",
                test: () => {
                    const animation = document.getElementById("test-css-animation");
                    return animation.style.animation ? "Animation running." : "Animation not running.";
                },
                demo: () => `<div class="demo"><div id="test-css-animation" style="width: 100px; height: 100px; background: orange; animation: spin 2s linear infinite;"></div></div>`
            },
            {
                feature: "JavaScript Alert",
                test: () => {
                    alert("Test alert!");
                    return "Alert displayed.";
                },
                demo: () => `<div class="demo"><button onclick="alert('Button clicked!')">Click Me</button></div>`
            },
            {
                feature: "LocalStorage",
                test: () => {
                    localStorage.setItem("test", "works");
                    return localStorage.getItem("test") === "works" ? "LocalStorage works." : "LocalStorage not working.";
                },
                demo: () => `<div class="demo"><div id="test-localstorage">LocalStorage test: ${localStorage.getItem("test") || "Not working."}</div></div>`
            },
            {
                feature: "Geolocation",
                test: () => {
                    return "geolocation" in navigator ? "Geolocation supported." : "Geolocation not supported.";
                },
                demo: () => `<div class="demo"><div id="test-geolocation">Geolocation: ${"geolocation" in navigator ? "Supported" : "Not supported"}</div></div>`
            }
        ];

        // Display Results
        const resultsTable = document.getElementById("results");
        results.forEach(({ feature, test, demo }) => {
            const { working, message, demo: demoContent } = testFeature(feature, test, demo);
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${feature}</td>
                <td class="${working ? "working" : "not-working"}">
                    ${working ? "✔️ Working" : "❌ Not Working: " + message}
                </td>
                <td>${demoContent || "No demo available."}</td>
            `;
            resultsTable.appendChild(row);
        });
    </script>
</body>
</html>
"""

HTML(html_content)
