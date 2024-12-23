#!/bin/bash
  
#SBATCH -J  job_name                          # 작업 이름 지정
#SBATCH -o  ./log/out.do_job_name.%j          # stdout 출력 파일 이름 (%j는 %jobId로 확장됨)
#SBATCH -e  ./log/err.do_job_name.%j          # stderr 출력 파일 이름 (%j는 %jobId로 확장됨)
#SBATCH -p  gpu-all                           # 큐 또는 파티션 이름 - gpu-all, gpu-3090, gpu-4090
#SBATCH -t  20:00:00                          # 최대 실행 시간 (hh:mm:ss) - 최대 7일
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --gres=gpu:2                          # 요청한 노드당 GPU 수
#SBATCH --nodelist=node03                     # 지정할 노드 번호

. /usr/share/modules/init/bash
source /opt/ohpc/pub/anaconda3/etc/profile.d/conda.sh
module  purge
module  load cuda/11.3                        # cuda 11.3 로드 

echo  $SLURM_SUBMIT_HOST
echo  $SLURM_JOB_NODELIST
echo  $SLURM_SUBMIT_DIR

echo  ### START ###

### cuda  test  ###

conda activate env                            # 환경 변경
python -m torch.distributed.launch --nproc_per_node 1 --master_port 21243 {command} # train.py -i {path/to/input} -o {path/to/output}  


date  ; echo  ##### END #####

