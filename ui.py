#!/usr/bin/python2
# -*- coding: utf-8 -*-

import re
import sys
from urllib import urlopen
import subprocess
if sys.getdefaultencoding() != 'utf-8':
	reload(sys)
	sys.setdefaultencoding('utf-8')
from Tkinter import *
import tkFont

class my_decorator:
	def __init__(self, function):
		self.function = function
	def __call__(self, *args):
		try:
			return self.function(*args)
		except Exception, e:
			res_text.insert(END, 'Error: %s\n' % e, 'red')

def get_regex_and_strs():
	return reg_entry.get(), str_text.get('1.0', END)

def do_cleanup_res():
	res_text.config(state=NORMAL)
	res_text.delete('1.0', END)
	res_text.config(state=DISABLED)

def do_cleanup_regex_and_strs():
	reg_entry.delete('0', END)
	str_text.delete('1.0', END)

def do_cleanup():
	do_cleanup_res()
	do_cleanup_regex_and_strs()
	his_text.config(state=NORMAL)
	his_text.insert(END, 'CLEAN\n', 'red')
	his_text.config(state=DISABLED)

def do_reg():
	if v.get() == 1: do_re_search()
	if v.get() == 2: do_re_findall()
	if v.get() == 3: do_re_sub()

def do_copy_res():
	str_text.delete('1.0', END)
	str_text.insert(END, res_text.get('1.0', END))
	his_text.config(state=NORMAL)
	his_text.insert(END, 'COPY result strings for testing\n', 'red')
	his_text.config(state=DISABLED)

@my_decorator
def do_get_html():
	url = url_entry.get()
	str_text.delete('1.0', END)
	html = urlopen(url).read()
	str_text.delete('1.0', END)
	str_text.insert(END, html)

@my_decorator
def do_get_cmd_output():
	cmd = cmd_entry.get()
	cmdlist = cmd.split()
	str_text.delete('1.0', END)
	str_text.insert(END, subprocess.check_output(cmdlist))

@my_decorator
def do_re_search():
	do_cleanup_res()
	res_text.config(state=NORMAL)
	regex, strs = get_regex_and_strs()
	try:
		res = re.search(regex, strs)
		if len(res.groups()) != 0:
			i = 1
			for item in res.groups():
				res_text.insert(END, '*** group %i ***\n' % i, 'maroon')
				i += 1
				res_text.insert(END, item + '\n\n', 'green')
		else:
			res_text.insert(END, res.group(), 'green')
	except:
		res_text.insert(END, '*** NO MATCH ***', 'red')
	res_text.config(state=DISABLED)
	his_text.config(state=NORMAL)
	his_text.insert(END, 'regex: ', 'maroon')
	his_text.insert(END, regex + '\n', 'green')
	his_text.insert(END, 'operation: ', 'maroon')
	his_text.insert(END, 're.search\n', 'green')
	his_text.config(state=DISABLED)

@my_decorator
def do_re_findall():
	do_cleanup_res()
	res_text.config(state=NORMAL)
	regex, strs = get_regex_and_strs()
	res = re.findall(regex, strs)
	if len(res) != 0:
		i  = 0
		for item in res:
			res_text.insert(END, '*** findall list %i ***\n' % i, 'maroon')
			i += 1
			res_text.insert(END, item + '\n\n', 'green')
	else:
		res_text.insert(END, '*** NO MATCH ***', 'red')
	res_text.config(state=DISABLED)
	his_text.config(state=NORMAL)
	his_text.insert(END, 'regex: ', 'maroon')
	his_text.insert(END, regex + '\n', 'green')
	his_text.insert(END, 'operation: ', 'maroon')
	his_text.insert(END, 're.findall\n', 'green')
	his_text.config(state=DISABLED)

@my_decorator
def do_re_sub():
	do_cleanup_res()
	res_text.config(state=NORMAL)
	regex, strs = get_regex_and_strs()
	rep_strs = rep_entry.get()
	res = re.sub(regex, rep_strs, strs)
	res_text.insert(END, res, 'green')
	res_text.config(state=DISABLED)
	his_text.config(state=NORMAL)
	his_text.insert(END, 'regex: ', 'maroon')
	his_text.insert(END, regex + '\n', 'green')
	his_text.insert(END, 'replacing: ', 'maroon')
	his_text.insert(END, rep_strs + '\n', 'blue')
	his_text.insert(END, 'operation: ', 'maroon')
	his_text.insert(END, 're.sub\n', 'green')
	his_text.config(state=DISABLED)
	his_text('regex: ', 'maroon')

if __name__ == '__main__':

	win = Tk()
	win.wm_title(sys.argv[0])

	myfont = tkFont.Font(family=u"文泉驿等宽微米黑", size=12, weight='normal')
	
	v = IntVar()

	l1 = Label(win, text='regular expression', font=myfont)
	l1.grid(row=0, column=0)
	reg_entry = Entry(win, font=myfont, fg='green')
	reg_entry.grid(row=1, column=0, columnspan=3, sticky=W+E+N+S)

	l2 = Label(win, text='replace strings(re.sub *ONLY*)', font=myfont)
	l2.grid(row=2, column=0)
	rep_entry = Entry(win, font=myfont, fg='blue')
	rep_entry.grid(row=3, column=0, columnspan=3, sticky=W+E+N+S)

	l3 = Label(win, text='select a method', font=myfont)
	l3.grid(row=4, column=0)
	r1 = Radiobutton(win, text='re.search', font=myfont, variable=v, value=1, width=30)
	r1.grid(row=5, column=0)
	r2 = Radiobutton(win, text='re.findall', font=myfont, variable=v, value=2, width=30)
	r2.grid(row=5, column=1)
	r3 = Radiobutton(win, text='re.sub', font=myfont, variable=v, value=3, width=30)
	r3.grid(row=5, column=2)
	
	l4 = Label(win, text='testing strings', font=myfont)
	l4.grid(row=6, column=0)
	str_text = Text(win, font=myfont, height=9)
	str_text.grid(row=7, column=0, columnspan=3, sticky=W+E+N+S)
	
	l5 = Label(win, text='results', font= myfont)
	l5.grid(row=8, column=0)
	res_text = Text(win, font=myfont, height=9, state=DISABLED)
	res_text.tag_config('green',  foreground='#008000')
	res_text.tag_config('maroon', foreground='#800000')
	res_text.tag_config('red',    foreground='#ff0000')
	res_text.grid(row=9, column=0, columnspan=3, sticky=W+E+N+S)

	l6 = Label(win, text='get strings from url:', font=myfont)
	l6.grid(row=10, column=0)
	url_entry = Entry(win, font=myfont, fg='blue')
	url_entry.insert(0, 'http://')
	url_entry.grid(row=11, column=0, columnspan=2, sticky=W+E+N+S)
	UrlButton = Button(win, text='Get html', fg='blue', font=myfont, command=do_get_html, width=30)
	UrlButton.grid(row=11, column=2)

	l7 = Label(win, text='get strings form cmd:', font=myfont)
	l7.grid(row=12, column=0)
	cmd_entry = Entry(win, font=myfont, fg='blue')
	cmd_entry.grid(row=13, column=0, columnspan=2, sticky=W+E+N+S)
	CmdButton = Button(win, text='Get output', fg='blue', font=myfont, command=do_get_cmd_output, width=30)
	CmdButton.grid(row=13, column=2)

	l8 = Label(win, text='histroy operations', font=myfont)
	l8.grid(row=0, column=3)
	his_text = Text(win, font=myfont, height=10, width=30, state=DISABLED)
	his_text.tag_config('green',  foreground='#008000')
	his_text.tag_config('maroon', foreground='#800000')
	his_text.tag_config('red',    foreground='#ff0000')
	his_text.tag_config('blue',   foreground='#0000ff')
	his_text.grid(row=1, column=3, rowspan=13, sticky=W+E+N+S)
	
	DoButton = Button(win, text='Do', fg='green', font=myfont, command=do_reg, width=30)
	DoButton.grid(row=14, column=0)
	CopyButton = Button(win, text='Copy result', fg='green', font=myfont, command=do_copy_res, width=30)
	CopyButton.grid(row=14, column=1)
	CleanButton = Button(win, text='Clean', fg='red', font=myfont, command=do_cleanup, width=30)
	CleanButton.grid(row=14, column=2)
	QuitButton = Button(win, text='Quit', fg='red', font=myfont, command=win.quit, width=30)
	QuitButton.grid(row=14, column=3)
	
	mainloop()