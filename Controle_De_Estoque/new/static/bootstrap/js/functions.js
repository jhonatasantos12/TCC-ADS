function aumentaValor(parm){
    var valor=document.getElementById(parm).value;
    valor++;
    document.getElementById(parm).value=valor;
}
function diminuiValor(parm){
    var valor=document.getElementById(parm).value;
    var number = parseInt(valor, 10);
    number--
    if (number <0)
    {
        document.getElementById(parm).value=0;   
    }
    else{
        document.getElementById(parm).value=number;   
    }
}