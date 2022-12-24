from django.shortcuts import render
import AI,activities
places = activities.build()
classes = {1:'empty',2:'sadness',3:'enthusiasm',4:'neutral',5:'worry',6:'surprise',7:'love',8:'fun',9:'hate',10:'happiness',11:'boredom',12:'relief',13:'anger'}
def Home(request):
    if request.method == 'POST':
        ans = AI.predict(request.POST.get('Message'))
        index = 0
        bigger = float(0)
        for i in range(len(ans)):
            ans[i] = float(ans[i])
            if bigger <  ans[i]:
              index = i
              bigger = ans[i]
        return render(request,'index.html',context={'message':ans,'items':places[classes[index + 1]]})
    return render(request,'index.html')