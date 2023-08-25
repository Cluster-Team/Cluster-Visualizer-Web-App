from django.shortcuts import render  
  
# Create your views here.  
from django.http import HttpResponse  
from django.template import loader
from plotly.offline import plot
import plotly.graph_objs as go
from pll.plotly_plot import *
from django.http import JsonResponse
import json
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
import logging
from .forms import EventsForm
import csv

res = []
  
def hello(request):
    target_plot = figure_ret_aff()
    # target_plot = 0

    #Return context to home page view
    context = {'target_plot': target_plot,}
    return render(request,'index.html',context)



    template = loader.get_template('index.html')
    return HttpResponse(template.render()) 
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  

def submit_matrix(request):
    if request.method == "POST":
        matrix = request.POST
        # print(int(matrix['damping']))
        # print(matrix_json)
        # matrix = json.loads(matrix_json)
        # Do something with the matrix data here, such as save it to a database
        res.clear()
        try:
            m = int(matrix['m'])
            n = int(matrix['n'])
            damping = matrix['damping'],
            iteration = matrix['iteration'],
            preference = matrix['preference'],
            # res = []
            for i in range(m):
                row = []
                for j in range(n):
                    value = request.POST.getlist('matrix['+str(i)+'][]')[j]
                    row.append(float(value))

                res.append(row)
            target_plot = figure_ret_aff(res,preference)
        except:
            target_plot=figure_ret_aff()    
            

        print(res)
        print(matrix)

        context = {'target_plot': target_plot}

        return JsonResponse(context)
    else:
        return JsonResponse({"status": "error"})
    
def submit_matrix2(request):
    if request.method == "POST":
        matrix = request.POST
        # print(int(matrix['damping']))
        # print(matrix_json)
        # matrix = json.loads(matrix_json)
        # Do something with the matrix data here, such as save it to a database
        res.clear()
        try:
            m = int(matrix['m'])
            n = int(matrix['n'])
            # res = []
            for i in range(m):
                row = []
                for j in range(n):
                    value = request.POST.getlist('matrix['+str(i)+'][]')[j]
                    row.append(float(value))

                res.append(row)
            target_plot = figure_ret_kmeans(res)
        except:
            target_plot=figure_ret_kmeans()    
            

        print(res)
        print(matrix)

        context = {'target_plot': target_plot}

        return JsonResponse(context)
    else:
        return JsonResponse({"status": "error"})
    
def submit_matrix3(request):
    if request.method == "POST":
        matrix = request.POST
        # print(int(matrix['damping']))
        # print(matrix_json)
        # matrix = json.loads(matrix_json)
        # Do something with the matrix data here, such as save it to a database
        res.clear()
        try:
            m = int(matrix['m'])
            n = int(matrix['n'])
            # res = []
            for i in range(m):
                row = []
                for j in range(n):
                    value = request.POST.getlist('matrix['+str(i)+'][]')[j]
                    row.append(float(value))

                res.append(row)
            target_plot = figure_ret_spec(res)
        except:
            target_plot=figure_ret_spec()    
            

        print(res)
        print(matrix)

        context = {'target_plot': target_plot}

        return JsonResponse(context)
    else:
        return JsonResponse({"status": "error"})
    


def upload_csv(request):
	# data = {}
	# if "GET" == request.method:
	# 	return render(request, "myapp/upload_csv.html", data)
    # if not GET, then proceed

	# try:
    # csv_file = request.FILES["csv_file"]
    
		# if not csv_file.name.endswith('.csv'):
		# 	messages.error(request,'File is not CSV type')
		# 	return HttpResponseRedirect(reverse("upload_csv"))
        # #if file is too large, return
		# if csv_file.multiple_chunks():
		# 	messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
		# 	return HttpResponseRedirect(reverse("upload_csv"))

		# file_data = csv_file.read().decode("utf-8")		

		# lines = file_data.split("\n")
		# #loop over the lines and save them in db. If error , store as string and then display
		# for line in lines:						
		# 	fields = line.split(",")
		# 	data_dict = {}
		# 	data_dict["name"] = fields[0]
		# 	data_dict["start_date_time"] = fields[1]
		# 	data_dict["end_date_time"] = fields[2]
		# 	data_dict["notes"] = fields[3]
		# 	try:
		# 		form = EventsForm(data_dict)
		# 		if form.is_valid():
		# 			form.save()					
		# 		else:
		# 			logging.getLogger("error_logger").error(form.errors.as_json())												
		# 	except Exception as e:
		# 		logging.getLogger("error_logger").error(repr(e))					
		# 		pass
	# except Exception as e:
	# 	logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
	# 	messages.error(request,"Unable to upload file. "+repr(e))

    if request.method == "POST":
        print(request.POST)
        
        csv_file = request.FILES["csv_file"]
        
        # if not csv_file.name.endswith('.csv'):
        #     messages.error(request,'File is not CSV type')
        #     return HttpResponseRedirect(reverse("upload_csv"))
        # #if file is too large, return
        # if csv_file.multiple_chunks():
        #     messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
        #     return HttpResponseRedirect(reverse("upload_csv"))


        # pd.read_csv(csv_file)
        iteration = int(request.POST['iteration']),
        preference = int(request.POST['preference']),

        iteration = list(iteration)[0]
        preference = list(preference)[0]
        print(iteration)

        file_data = csv_file.read().decode("utf-8")
        f = open("hello00.csv","w")
        f.write(file_data)
        f.close()
        df = pd.read_csv("hello00.csv",index_col = 0,header=0)

        res = df.to_numpy().tolist()
        print(type(res[0][0]))
        # print(res)


        # lines = file_data.split("\n")
        # res = []
        # i = 0
        # for line in lines:
        #     if i == 0:
        #         continue
        #     # print(line)
        #     fields = line.split(",")
        #     res.append(fields)
        #     i = i +1
        

		# fields = line.split(",")



        # print(file_data)
        
        target_plot = figure_ret_aff(res,preference,iteration)
        context = {'target_plot': target_plot}

        return JsonResponse(context)
    else:
        return JsonResponse({"status": "error"})


	# return HttpResponseRedirect(reverse("upload_csv"))


def upload_csv2(request):

    if request.method == "POST":
        print(request.POST)
        
        csv_file = request.FILES["csv_file2"]
        iteration = int(request.POST['iteration']),
        cluster = int(request.POST['cluster']),

        iteration = list(iteration)[0]
        cluster = list(cluster)[0]

        file_data = csv_file.read().decode("utf-8")
        f = open("hello02.csv","w")
        f.write(file_data)
        f.close()
        df = pd.read_csv("hello02.csv",index_col = 0,header=0)

        res = df.to_numpy().tolist()
        print(type(res[0][0]))

        # target_plot = figure_ret_kmeans(res)
        target_plot = figure_ret_kmeans(res,iteration,10,cluster)
        context = {'target_plot': target_plot}

        return JsonResponse(context)
    else:
        return JsonResponse({"status": "error"})
    
def upload_csv3(request):

    if request.method == "POST":
        print(request.POST)
        
        csv_file = request.FILES["csv_file3"]
        epsilon = int(request.POST['epsilon']),
        cluster = int(request.POST['cluster']),

        epsilon = list(epsilon)[0]
        cluster = list(cluster)[0]

        file_data = csv_file.read().decode("utf-8")
        f = open("hello03.csv","w")
        f.write(file_data)
        f.close()
        df = pd.read_csv("hello03.csv",index_col = 0,header=0)

        res = df.to_numpy().tolist()
        print(type(res[0][0]))

        
        target_plot = figure_ret_spec(res, epsilon,cluster)
        context = {'target_plot': target_plot}

        return JsonResponse(context)
    else:
        return JsonResponse({"status": "error"})
