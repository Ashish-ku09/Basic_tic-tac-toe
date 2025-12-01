<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Projects - Calculator & Tic-Tac-Toe</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; margin: 0; padding: 20px; max-width: 800px; margin: 0 auto; background: #f5f5f5; }
        .container { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; text-align: center; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        h2 { color: #34495e; border-left: 5px solid #e74c3c; padding-left: 15px; }
        h3 { color: #2980b9; }
        code { background: #ecf0f1; padding: 2px 6px; border-radius: 4px; font-family: 'Courier New', monospace; }
        pre { background: #2c3e50; color: #ecf0f1; padding: 20px; border-radius: 8px; overflow-x: auto; }
        .project-card { background: #f8f9fa; padding: 25px; margin: 20px 0; border-radius: 8px; border-left: 5px solid #27ae60; }
        .badge { display: inline-block; background: #3498db; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; margin: 2px; }
        ul { padding-left: 20px; }
        .demo { background: #e8f5e8; padding: 15px; border-radius: 5px; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Python Mini Projects</h1>
        <p><strong>Simple Calculator & Tic-Tac-Toe Game</strong> - Beginner-friendly Python projects built by a Data Science student.</p>
        
        <div class="project-card">
            <h2>📱 Simple Calculator</h2>
            <p>A command-line calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division.</p>
            
            <h3>Features</h3>
            <ul>
                <li class="badge">Addition (+)</li>
                <li class="badge">Subtraction (-)</li>
                <li class="badge">Multiplication (×)</li>
                <li class="badge">Division (÷)</li>
                <li class="badge">User-friendly interface</li>
            </ul>
            
            <div class="demo">
                <strong>Demo:</strong><br>
                <code>Enter operation: 15 + 7 → Result: 22</code>
            </div>
        </div>

        <div class="project-card">
            <h2>🎮 Tic-Tac-Toe Game</h2>
            <p>Classic 3x3 Tic-Tac-Toe game for two players (X vs O) with win detection and tie handling.</p>
            
            <h3>Features</h3>
            <ul>
                <li class="badge">Visual board display</li>
                <li class="badge">Input validation</li>
                <li class="badge">Win/tie detection</li>
                <li class="badge">Row/column/diagonal checks</li>
                <li class="badge">Easy row,col input (1,2)</li>
            </ul>
            
            <div class="demo">
                <strong>Sample board:</strong><br>
                <pre>  1   2   3
1 |   |   |  
  ---------
2 |   |   |  
  ---------
3 |   |   |  
</pre>
            </div>
        </div>

        <h2>🛠️ How to Run</h2>
        <ol>
            <li><strong>Prerequisites:</strong> Python 3.6+ installed</li>
            <li>Copy-paste these exact commands in VS Code Terminal:</li>
        </ol>
        <pre><code>cd "your-project-folder"
python calculator.py
# OR
python tic-tac-toe.py</code></pre>

        <h2>📥 How to Clone & Try</h2>
        <ol>
            <li>Open Terminal/Command Prompt</li>
            <li>Run these commands:
                <pre><code>git clone https://github.com/YOUR_USERNAME/simple-python-projects.git
cd simple-python-projects
python calculator.py</code></pre>
            </li>
            <li>Replace <code>YOUR_USERNAME</code> with your GitHub username</li>
        </ol>

        <h2>📁 Project Structure</h2>
        ```
        simple-python-projects/
        ├── calculator.py
        ├── tic-tac-toe.py
        ├── README.html     ← This file!
        └── README.md
        ```

        <h2>🎓 About Me</h2>
        <p>Built by Ashish - BSC Computer Science graduate, currently studying <strong>Data Science with Gen AI</strong> in Hyderabad. Practicing Python fundamentals through fun projects!</p>
        
        <p style="text-align: center; color: #7f8c8d; font-size: 0.9em;">
            <strong>Happy Coding! 🚀</strong> | Made with ❤️ for learning
        </p>
    </div>
</body>
</html>
