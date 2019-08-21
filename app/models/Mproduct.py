import time
class ModelProduct:
    def __init__(self, methdPost):

        self.methdPost = methdPost
        #self.methdPost.setdefault('Producto_Id', -1)

        self.Categoria_id = self.methdPost["Categoria_id"]
        self.Titulo=self.methdPost["Titulo"]
        self.Descripcion=self.methdPost["Descripcion"]
        self.Estado=self.methdPost["Estado"]
        self.Referencia_Amazon=self.methdPost["Referencia_Amazon"]
        self.Creado_Por=self.methdPost["Creado_Por"]
        self.Modificado_Por=self.methdPost["Modificado_Por"]
        self.Fecha_Creacion=self.methdPost["Fecha_Creacion"]
        self.Fecha_Actualizacion =self.methdPost["Fecha_Actualizacion"]


    def validateValue(self):
        Categoria_id = int(self.Categoria_id)
        if type(Categoria_id)  != int:
            raise ValueError("Digita numeros")
        return {"Comer":"Es lista"}

        if self.Fecha_Creacion != time.strftime:
            raise ValueError("Las fechas no coiciden")
