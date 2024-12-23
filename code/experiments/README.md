# GPU Cluster 접속 방법

## Jupyter Notebook 사용 (VSCode 활용)

### VSCode 로컬에 설치 후 VSCode SSH 연결하는 법
1. **VSCode에서 해당 노드 (예: node03)로 접속**
   - Extensions > Remote-SSH 설치
   - VSCode > Ctrl+Shift+P 또는 F1 > Remote-SSH: Open SSH Configuration File > `C:/Users/user/.ssh/config`

   ```plaintext
   Host GPU_master
       HostName 147.46.30.109
       User shhan
       port 7777
       # 각 행에 주석이 있으면 안됨. 주석 넣으려면 다음 줄로!

   Host node03 # 할당된 노드
       HostName node03
       User username
       ForwardAgent yes
       ProxyJump GPU_master
       ServerAliveInterval 60
  ```

   - F1 > Remote-SSH: Connect to Host > node03 > 비밀번호 입력 (두 번)
   
2. **가상환경 Kernel 선택 후 GPU 사용 가능 여부 확인**
   - 예: ```torch.cuda.is_available() >> True```

3. **Slurm 상에서 Jupyter 사용이 인식되지 않으므로, 반드시 아래 명령어 실행**
  ```plaintext
   srun --gres=gpu --nodelist=node03 --pty bash -i
  ```

4. **가상환경 이름이 ~/.conda로 시작하지 않는 경우**
   - ```F1 > Select Notebook Kernel > Python Environments``` 에서 선택
