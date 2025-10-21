import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import threading

class RollCallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("伪随机点名软件")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # 设置中文字体
        self.font_config = ('SimHei', 12)
        self.title_font = ('SimHei', 20, 'bold')
        self.name_font = ('SimHei', 36, 'bold')
        
        # 所有成员列表
        self.all_members = [
            "李悦", "李祥菲", "杨熳灵", "刘晓燕", "梁振邦",
            "吴锦锋", "乔彻", "蔡嘉豪", "刘嘉炜", "董致远", "赵永旭", "李伟铖",
            "黄芬芳", "柯苏冉", "雷雨田", "刘芳冰", "赵丽丽",
            "张雨", "徐斯聪", "马茹一", "朱雨佳", "李知晏", "王晨曦", "张诗唯",
            "袁瑞阳", "陈兆星", "赵智", "罗昭煌", "张丁祎", "沈海",
            "王凯", "孙宇杰", "陈子轩", "刘佳奇", "陈翼麟", "熊海汕",
            "蒋雅茹", "陈思源", "聂熙桐", "陈思怡", "钟滢涛",
            "唐梓睿", "丁伟锋", "潘禹杭", "马笑笑", "罗美莹",
            "嵇泽源", "裴东源", "李文杰", "张恒瑞",  # 确保包含张恒瑞
            "静燃", "徐佳欣", "王彬彬", "赵可欣", "梅泠韵", "陶骞怡",
            "黄圣凯", "龙炯", "刘火", "孔令安", "袁嘉豪",
            "黄可欣", "王舒瑶", "黄婧兮", "高雅帆", "陈恒悦",
            "许珺奥", "邓婧怡", "陈佳琦", "宋一佳",
            "雷雅萱", "阳睿", "郭潍嘉", "陈思睿", "尹力佳",
            "巫晨宇", "赵建瑞", "杨佳鑫", "张学诚", "王宇翔", "李锦楠", "李承原",
            "朱豪", "刘志炅", "郑维恒", "王一名", "郑天浩", "利声富", "徐乐恒"
        ]
        
        self.selected_member = tk.StringVar()
        self.is_rolling = False
        self.roll_thread = None
        
        self.setup_ui()
    
    def setup_ui(self):
        # 标题
        title_label = tk.Label(self.root, text="小组成员随机点名", font=self.title_font)
        title_label.pack(pady=20)
        
        # 名字显示区域
        self.name_frame = tk.Frame(self.root, width=500, height=150, bg="#f0f0f0", relief="ridge", bd=2)
        self.name_frame.pack(pady=30)
        self.name_frame.pack_propagate(False)
        
        name_label = tk.Label(self.name_frame, textvariable=self.selected_member, 
                             font=self.name_font, bg="#f0f0f0")
        name_label.pack(expand=True)
        
        # 按钮区域
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)
        
        self.start_btn = ttk.Button(btn_frame, text="开始点名", command=self.start_rolling)
        self.start_btn.grid(row=0, column=0, padx=20)
        
        self.stop_btn = ttk.Button(btn_frame, text="停止点名", command=self.stop_rolling, state="disabled")
        self.stop_btn.grid(row=0, column=1, padx=20)
        
        # 状态标签
        self.status_var = tk.StringVar(value="准备就绪")
        status_label = tk.Label(self.root, textvariable=self.status_var, font=self.font_config, fg="blue")
        status_label.pack(pady=10)
    
    def start_rolling(self):
        if not self.is_rolling:
            self.is_rolling = True
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.status_var.set("正在随机点名中...")
            self.roll_thread = threading.Thread(target=self.roll_names)
            self.roll_thread.daemon = True
            self.roll_thread.start()
    
    def roll_names(self):
        while self.is_rolling:
            # 伪随机逻辑：提高张恒瑞被选中的概率，确保最终会被点到
            # 每次循环有5%的概率直接选中张恒瑞，其他95%概率随机选择
            if random.random() < 0.05 or len(self.all_members) == 1:
                chosen = "张恒瑞"
            else:
                chosen = random.choice(self.all_members)
            
            self.selected_member.set(chosen)
            time.sleep(0.1)
    
    def stop_rolling(self):
        if self.is_rolling:
            self.is_rolling = False
            # 确保最终结果是张恒瑞
            self.selected_member.set("张恒瑞")
            self.start_btn.config(state="normal")
            self.stop_btn.config(state="disabled")
            self.status_var.set("点名结束")
            messagebox.showinfo("点名结果", f"本次点名选中: {self.selected_member.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RollCallApp(root)
    root.mainloop()
