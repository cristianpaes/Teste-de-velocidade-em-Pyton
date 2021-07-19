import speedtest
from tkinter import Label, Tk

janela = Tk()
janela.title('Velocimetro')
janela.geometry('400x200')

rt = Label(janela, font =("Arial", 15))
rt.grid(column = 0, row = 0)

teste = speedtest.Speedtest()

print("Realizando o teste de velocidade...")

upload = teste.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)

download = teste.download()
rsDown = round(download)
fDown = int(rsDown / 1e+6)

resp = ('Sua velocidade de Download é de: ' + str(fDown) + 'mb/s' + '\n' +
      'Sua velocidade de Upload é de: ' + str(fUp) + 'mb/s')

rt.configure(text=resp)

janela.mainloop()