import re
import hashlib
import tkinter as tk
import tkinter.messagebox as messagebox

class KeyGenerator(object):
    def __init__(self, root):
        self.root = root
        self.render()
        
    def check_email(self, email):
        if(re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,}$', email)):
            return True
        else:
            return False

    def popup_msg(self, mode, title, msg):
        if mode == 0:
            messagebox.showinfo(str(title), str(msg))
        elif mode == 1:
            messagebox.showwarning(str(title), str(msg))
        elif mode == 2:
            messagebox.showerror(str(title), str(msg))
            
    def print_msg(self, msg):
        self.text_field.config(state='normal')
        self.text_field.delete(0, tk.END)
        self.text_field.insert(tk.END, str(msg))
        self.text_field.config(state='readonly')
        
    def generate_key(self):
        username = self.entry_field_1.get()
        if username == '':
            self.popup_msg(2, 'Error', 'Empty Username!')
            return False
        
        email = self.entry_field_2.get()
        if email == '':
            self.popup_msg(2, 'Error', 'Empty Email!')
            return False
        if not self.check_email(email):
            self.popup_msg(2, 'Error', 'Invalid Email!')
            return False
        
        if self.entry_field_3.get() != '':
            private_string_1 = self.entry_field_3.get()
        else:
            private_string_1 = "iWyIaL99x62K3KtwBoElZ3np0nI6HNt63yAdpLvljji1V9hWg6"
            
        if self.entry_field_4.get() != '':
            private_string_2 = self.entry_field_4.get()
        else:
            private_string_2 = "IccAT7LkhqWvtJgP0dxXZRoor17FtZZ3np0nI6HNifAC8KMg1f"
        private_string_1 = hashlib.sha256((private_string_1).encode()).hexdigest()
        private_string_2 = hashlib.sha256((private_string_2).encode()).hexdigest()
        string = username + private_string_1 + email + private_string_2
        phase_1 = hashlib.sha512(string.encode()).hexdigest()
        phase_2 = hashlib.sha256((phase_1+private_string_1).encode()).hexdigest()
        phase_3 = hashlib.sha1((phase_2+private_string_2).encode()).hexdigest()
        t = hashlib.md5(phase_3.encode()).hexdigest().lower()
        t = t.replace('0','T').replace('o','T').replace('1','D').replace('l','D').replace('i','D').upper()
        #print(t)
        result = ''
        for i in range(0,28,4):
            result += t[i:i+4] + '-'
        result += t[28:32]
        if str(result) == str(self.entry_field_5.get()):
            self.print_msg('Product activated!')
        else:
            self.print_msg('Activation failed!')

    def render(self):
        tk.Label(self.root, text='KEY VERIFIER').grid(row=1, column=1, columnspan=2)
        tk.Label(self.root, text='Username*').grid(row=2, column=1)
        tk.Label(self.root, text='Email*').grid(row=3, column=1)
        tk.Label(self.root, text='Private String 1').grid(row=4, column=1)
        tk.Label(self.root, text='Private String 2').grid(row=5, column=1)
        tk.Label(self.root, text='Key').grid(row=6, column=1)

        self.entry_field_1 = tk.Entry(self.root, width=30)
        self.entry_field_2 = tk.Entry(self.root, width=30)
        self.entry_field_3 = tk.Entry(self.root, width=30)
        self.entry_field_4 = tk.Entry(self.root, width=30)
        self.entry_field_5 = tk.Entry(self.root, width=30)
        self.entry_field_1.grid(row=2, column=2, sticky='news')
        self.entry_field_2.grid(row=3, column=2, sticky='news')
        self.entry_field_3.grid(row=4, column=2, sticky='news')
        self.entry_field_4.grid(row=5, column=2, sticky='news')
        self.entry_field_5.grid(row=6, column=2, sticky='news')
        
        self.text_field = tk.Entry(self.root, width=30, justify='center')
        self.text_field.grid(row=7, column=1, columnspan=2, sticky='news')
        self.text_field.config(state='readonly')
        
        tk.Button(self.root, text='ACTIVATE', command=self.generate_key).grid(row=8, column=1, columnspan=2, sticky='news')


root = tk.Tk()
root.title('Key Generator')
root.resizable(False, False)
KeyGenerator(root)
root.mainloop()
