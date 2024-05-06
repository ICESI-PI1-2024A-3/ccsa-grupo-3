

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from postgraduateManagement.models import Contrato, Docente, TipoContrato, EstadoContrato
from django.http import HttpResponseBadRequest, HttpResponseServerError

@login_required
def viewContract(request):
    contracts= Contrato.objects.all()
    teacher= Docente.objects.all()
    return render(request, "viewcontract.html", {"contract": contracts, "person":teacher})

@login_required
def editContract(request, codigo):
    contract= Contrato.objects.get(codigo=codigo)
    estado= EstadoContrato.objects.all()
    tipoContrato=TipoContrato.objects.all()
    docente= Docente.objects.all()
    return render(request,"edit_contract.html",{"contract":contract,"estado":estado,"tipoContrato":tipoContrato,"docente":docente})

@login_required
def editingContract(request):
    if request.method == 'POST':
        try:
            codigo = request.POST['txtCodigo']
            fecha_elaboracion = request.POST['fecha_elaboracion']
            tipo_contrato = request.POST['tipo_contrato']
            estado_contrato = request.POST['estado_contrato']
            docente = request.POST['docente']
            
            
            estadoObject = EstadoContrato.objects.get(id=estado_contrato)
            tipoContratoObject = TipoContrato.objects.get(codigo=tipo_contrato)
            docenteObject = Docente.objects.get(cedula=docente)
            
            contract= Contrato.objects.get(codigo=codigo)
            
            contract.fecha_elaboracion=fecha_elaboracion
            contract.tipo_contrato=tipoContratoObject
            contract.estado_contrato=estadoObject
            contract.docente=docenteObject
            
            contract.save()
            return redirect('/viewContract')
        except Exception as a:
            return HttpResponseServerError(f"Error: {a}")
        else:
            return HttpResponseBadRequest("Método no permitido")
    
    
    
