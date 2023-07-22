translator = Translator()
translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
Output_text.delete(1.0, END)
Output_text.inset(END, translated.text)