import os   # 운영체제 관련 기능
import shutil   # 파일, 디렉터리 복사 및 이동
import json
from datetime import datetime
from pathlib import Path    # 파일 경로를 객체지향적으로 다룸 (설치 필요)
import zipfile  # 백업 파일 압축에 사용

class SmartBackup : 
    def __init__(self, source_dir, backup_dir) :
        self.source_dir = Path(source_dir)
        self.backup_dir = Path(backup_dir)  # path 객체로 저장
        self.backup_dir.mkdir(exist_ok=True)    # 없으면 생성, 이미 있으면 pass
        self.history_file = self.backup_dir / 'backup_history.json'
        self.load_history() # 기존 파일 백업 히스토리를 가져옴

    def load_history(self) :    # 백업 히스토리 있는지 확인, 있으면 불러와서 dict 형태로 변환, 없으면 빈 dict
        if self.history_file.exists() :
            with open(self.history_file, 'r') as f :
                self.history = json.load(f)
        else :
            self.history = {}

    def save_history(self) :
        with open(self.history_file, 'w') as f :
            json.dump(self.history, f, indent = 2)

    def need_backup(self, file_path) :  # 백업이 필요한지 판단 - 문자열로 변환해서 확인
        str_path = str(file_path) 
        if str_path not in self.history :
            return True

        last_modified = file_path.stat().st_mtime
        return last_modified > self.history[str_path]   # 마지막 수정일보다 최신이라면 True 반환
    
    def backup(self, compress = False) :
        backup_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        if compress :
            backup_path = self.backup_dir / f'backup_{backup_time}.zip'
            with zipfile.ZipFile(backup_path, 'w') as zf :
                for file_path in self.source_dir.rglob('*') :
                    if file_path.is_file() and self.need_backup(file_path) :
                        arcname = file_path.relative_to(self.source_dir)    # source directory 기준 상대 경로 구함
                        zf.write(file_path, arcname)
                        self.history[str(file_path)] = file_path.stat().st_mtime    # 히스토리 업데이트
                        print(f"백업 : {arcname}")  # 백업된 파일명 출력, 진행 상황 확인

                    else :
                        backup_path = self.backup_dir / f'backup_{backup_time}'
                        backup_path.mkdir()

                        for file_path in self.source_dir.rglob('*') :
                            if file_path.is_file() and self.need_backup(file_path):
                                relative_path = file_path.relative_to(self.source_dir)
                                dest_path = backup_path / relative_path
                                dest_path.parent.mkdir(parents=True, exist_ok=True)
                                shutil.copy2(file_path, dest_path)
                                self.history[str(file_path)] = file_path.stat().st_mtime
                                print(f"백업: {relative_path}")

                    self.save_history()
                    print(f"\n백업 완료: {backup_path}")


backup = SmartBackup('my_project', 'backups')
# backup.backup(compress=True)
backup.backup()

                                


    
