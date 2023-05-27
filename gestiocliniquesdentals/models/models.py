# -*- coding: utf-8 -*-

from odoo import models, fields, api
# class usuari(models.Model):
#      _name = 'gestiocliniquesdentals.usuari'
#      _description = 'gestiocliniquesdentals.gestiocliniquesdentals'

#      name = fields.Char()
#      value = fields.Integer()

#***** USUARIS ************************************************************************

class pacient(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'All information from patient'

    #dades personals
    photo = fields.Image()
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    dateborn = fields.Date()
    years = fields.Integer(compute="_get_calculEdad")

    #relacions
    pacient_historia = fields.Many2one(comodel_name='gestiocliniquesdentals.historia_medica')
    pacient_anamnesis = fields.Many2one(comodel_name='gestiocliniquesdentals.anamnesis')

    #pacient_higienista = fields.Many2many(comodel_name='gestiocliniquesdentals.higienista', relation='pacientHigienista')
    #pacient_doctor = fields.Many2many(comodel_name='gestiocliniquesdentals.doctor', relation='pacientDoctor')
    # pacient_auxiliar = fields.Many2many(comodel_name='gestiocliniquesdentals.auxiliar', relation='pacientAuxiliar')
    # pacient_administratiu = fields.Many2many(comodel_name='gestiocliniquesdentals.administratiu', relation='pacientAdministratiu')
    # pacient_director = fields.Many2many(comodel_name='gestiocliniquesdentals.director', relation='pacientDirector')
    # pacient_subdirector = fields.Many2many(comodel_name='gestiocliniquesdentals.subdirector', relation='pacientSubdirector')
    # pacient_altres = fields.Many2many(comodel_name='gestiocliniquesdentals.altres', relation='pacientAltres')

    #funcions
    @api.depends('dateborn')
    def _get_calculEdad(self):
        for t in self:
            if (t.dateborn):
                dataactual = fields.Date.from_string(fields.Date.today())
                datanaixement = fields.Date.from_string(t.dateborn)

                t.years = ((dataactual - datanaixement).days)/365
            else:
                t.years = 0


class profesional(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'All information from patient'

    name = fields.Char()


class doctor(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'All information from patient'

    #personal dates
    photo = fields.Image()
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    dateborn = fields.Date()
    street = fields.Char()
    city = fields.Char()
    val = fields.Char()
    zip = fields.Char()
    #state_id = fields.Many2one(comodel_name='res.country.state')


    #dades profesionals
    categoria = fields.Selection([("1","Doctor"), ("2","Higienista"), ("3","Auxiliar"), ("4","Director"), ("5","Subdirector"), ("6","Administratiu"), ("7","Altres")])
    num_colegiat = fields.Char()
    especialitat = fields.Selection([("1", "General"), ("2", "Cirujia"), ("3", "Ortodoncia"), ("4", "Odontopediatra"), ("5","Estética")])


    #relacions
    #doctor_pacient = fields.Many2many(comodel_name='gestiocliniquesdentals.pacient')

class higienista(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'All information from patient'

    #personal dates
    photo = fields.Image()
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    dateborn = fields.Date()
    
    #relacions
    #higienista_pacient = fields.Many2many(comodel_name='gestiocliniquesdentals.pacients')



class auxiliar(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'All information from patient'

    #personal dates
    photo = fields.Image()
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    dateborn = fields.Date()

    #relacions
    #auxiliar_pacient = fields.Many2many(comodel_name='gestiocliniquesdentals.pacients')

class administratiu(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'All information from patient'

    #personal dates
    photo = fields.Image()
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    dateborn = fields.Date()

    #relacions
    #administratiu_pacient = fields.Many2many(comodel_name='gestiocliniquesdentals.pacients')
    

class director(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'All information from patient'

    #personal dates
    photo = fields.Image()
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    dateborn = fields.Date()

    #relacions
    #director_pacient = fields.Many2many(comodel_name='gestiocliniquesdentals.pacients')

class subdirector(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'All information from patient'

    #personal dates
    photo = fields.Image()
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    dateborn = fields.Date()

    #relacions
    #subdirector_pacient = fields.Many2many(comodel_name='gestiocliniquesdentals.pacients')

class altres(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'All information from patient'

    #personal dates
    photo = fields.Image()
    name = fields.Char()
    surname1 = fields.Char()
    surname2 = fields.Char()
    dateborn = fields.Date()

    #relacions
    #altres_pacient = fields.Many2many(comodel_name='gestiocliniquesdentals.pacients')



#***** DOCUMENTS MÉDICS ****************************************************************

class historia_medica(models.Model):
    _name = 'gestiocliniquesdentals.historia_medica'
    _description = 'Informació mèdica del pacient'

    #personal dates
    id_historia = fields.Integer()
    data_alta = fields.Date()
    descripcio = fields.Text()

    #relacions
    historia_entrada = fields.Many2many(comodel_name='gestiocliniquesdentals.entrada', relation="historiaEntrada")
    historia_pacient = fields.One2many(comodel_name='res.partner', inverse_name="pacient_historia")

class entrada(models.Model):
    _name = 'gestiocliniquesdentals.entrada'
    _description = 'entrada dels actes que se li realitzen al pacient'

    #personal dates
    id_entrada = fields.Integer()
    id_usuari = fields.Integer()
    data_entrada = fields.Date()
    descripcio_curta = fields.Char()
    descripcio_llarga = fields.Text()

    #relacions
    entrada_historia = fields.Many2many(comodel_name='gestiocliniquesdentals.historia_medica', relation="historiaEntrada")

class anamnesis(models.Model):
    _name = 'gestiocliniquesdentals.anamnesis'
    _description = 'anamnesis del pacient'

    #personal dates
    id_anamnesis = fields.Char()
    data_alta_anam = fields.Date()
    #alergies
    latex = fields.Boolean()
    paracetamol = fields.Boolean()
    ibuprofeno = fields.Boolean()
    altres_alergies = fields.Char()
    #malalties
    covid = fields.Boolean()
    hepatits = fields.Boolean()
    vih = fields.Boolean()
    altres_malalties = fields.Char()

    #relacions
    anamnesis_pacient= fields.Many2one(comodel_name='res.partner')


#***** AGENDES I ORGANITZACIÓ **********************************************************

class agenda(models.Model):
    _name = 'gestiocliniquesdentals.agenda'
    _description = 'agenda general'

    #personal dates
    name = fields.Char()

class cita(models.Model):
    _name = 'gestiocliniquesdentals.cita'
    _description = 'cites de la agenda i del usuari en concret'

    #personal dates
    name = fields.Char()


#***** TRACTAMENTS I PRODUCTES *********************************************************

# class tractament(models.Model):
#     _name = 'sale.order.line'
#     _inherit = 'sale.order.line'

#     _description = 'Tractaments que es realitzen en la clínica'

#     #personal dates
#     name = fields.Char()

# class pressupost(models.Model):
#     _name = 'sale.order'
#     _inherit = 'sale.order'

#     _description = 'Presupostos que es realitzen als pacients'

#     #personal dates
#     name = fields.Char()

# class linies_pressupost(models.Model):
#     _name = 'sale.order.line'
#     _inherit = 'sale.order.line'

#     _description = 'Tractaments que es realitzen en la clínica que es detallen en el pressupost'

#     #personal dates
#     name = fields.Char()


