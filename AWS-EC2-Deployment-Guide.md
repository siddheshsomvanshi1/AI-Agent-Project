# 🚀 Deployment Guide: AI Agent on AWS EC2

This guide walks you through deploying the **FastAPI + React + Ollama** application on an AWS EC2 instance.

## Prerequisites
- AWS Account
- Basic knowledge of terminal/SSH
- EC2 Instance (Ubuntu 24.04 LTS recommended)

---

## Step 1: Launch EC2 Instance
1.  **OS**: Ubuntu Server 24.04 LTS (recommended)
2.  **Instance Type**:
    *   **Minimum**: `t3.medium` (2 vCPU, 4GB RAM) - LLaMA models require significant RAM.
    *   **Recommended**: `t3.large` or `g4dn.xlarge` (if GPU acceleration is needed).
3.  **Storage**: At least **20GB gp3** (Ollama models and system dependencies take space).
4.  **Security Group (Firewall)**:
    *   **SSH (22)** - Your IP (for access)
    *   **HTTP (80)** - Anywhere (for the web app)
    *   **Custom TCP (5000)** - Anywhere (Optional, for testing backend directly)

---

## Step 2: Connect and Install Dependencies
SSH into your instance:
```bash
ssh -i "your-key.pem" ubuntu@your-ec2-ip
```

Update system and install required tools:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv nodejs npm nginx git
```

*Note: If the installed Node.js version is too old (check with `node -v`), install a newer version using nvm:*
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install 20
node -v  # Should be v20.x.x or higher
```

---

## Step 3: Install and Setup Ollama
1.  Install Ollama:
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```

2.  Start Ollama service (if not running):
    ```bash
    sudo systemctl start ollama
    sudo systemctl enable ollama
    ```

3.  Pull the LLaMA 3.2 model:
    ```bash
    ollama pull llama3.2:latest
    ```
    *This might take a few minutes depending on internet speed.*

---

## Step 4: Clone Repository and Setup Backend
1.  **Clone the repository**:
    ```bash
    git clone <your-github-repo-url>
    cd AI-Agent-Project
    ```
    *(Replace `<your-github-repo-url>` with your actual repository URL)*

2.  **Setup Python Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Test the Backend**:
    ```bash
    python3 app.py
    ```
    *You should see "Uvicorn running on http://0.0.0.0:5000". Press `Ctrl+C` to stop it.*

5.  **Run Backend in Background**:
    We will use `nohup` to keep it running even after you disconnect.
    ```bash
    nohup python3 app.py > backend.log 2>&1 &
    ```
    *To stop it later, use `pkill -f app.py`.*

---

## Step 5: Setup Frontend
1.  **Navigate to frontend directory**:
    ```bash
    cd frontend
    ```

2.  **Install Node Dependencies**:
    ```bash
    npm install
    ```

3.  **Build for Production**:
    This compiles your React code into static HTML/CSS/JS files.
    ```bash
    npm run build
    ```
    *This creates a `dist` folder.*

---

## Step 6: Configure Nginx (Reverse Proxy)
We will use Nginx to serve the frontend on port 80 and forward API requests to the backend on port 5000.

1.  **Edit the default Nginx configuration**:
    ```bash
    sudo nano /etc/nginx/sites-available/default
    ```

2.  **Delete everything and paste the following**:
    *(Update the root path if your folder name is different)*

    ```nginx
    server {
        listen 80;
        server_name _;

        # Serve Frontend (React Build)
        location / {
            root /home/ubuntu/AI-Agent-Project/frontend/dist;
            index index.html;
            try_files $uri $uri/ /index.html;
        }

        # Proxy Backend API
        location /chat {
            proxy_pass http://localhost:5000;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }
    }
    ```

3.  **Save and Exit**: Press `Ctrl+X`, then `Y`, then `Enter`.

4.  **Test and Restart Nginx**:
    ```bash
    sudo nginx -t
    sudo systemctl restart nginx
    ```

---

## Step 7: Access Your App
Open your web browser and enter your EC2 instance's Public IP:
`http://<your-ec2-public-ip>`

🎉 **Congratulations! Your AI Agent is now live!**

---

## 🛠 Troubleshooting
*   **Backend not working?** Check logs: `cat ~/AI-Agent-Project/backend.log`
*   **502 Bad Gateway?** This means Nginx can't talk to the backend. Ensure `app.py` is running (`ps aux | grep python`).
*   **Permission Denied?** Ensure Nginx can read the files: `sudo chmod -R 755 /home/ubuntu/AI-Agent-Project`
