from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Modelos.Candidatos import Candidatos

class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidatos = RepositorioCandidatos()

    def index(self):
        return self.repositorioCandidatos.findAll()

    def create(self,elCandidato):
        nuevoCandidato = Candidatos(elCandidato)
        return self.repositorioCandidatos.save(nuevoCandidato)

    def show(self,id):
        elCandidato = Candidatos(self.repositorioCandidatos.findById(id))
        return elCandidato.__dict__

    def update(self, id, elCandidato):
        candidatoActual = Candidatos(self.repositorioCandidatos.findById(id))
        candidatoActual.cedula = elCandidato["cedula"]
        candidatoActual.nombre = elCandidato["nombre"]
        candidatoActual.apellido = elCandidato["apellido"]
        return self.repositorioCandidatos.save(candidatoActual)

    def delete(self, id):
        return self.repositorioCandidatos.delete(id)