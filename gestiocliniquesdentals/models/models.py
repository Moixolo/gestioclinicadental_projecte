# -*- coding: utf-8 -*-


from odoo import models, fields, api


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

    is_pacient = fields.Boolean()
    is_sanitari = fields.Boolean()
    is_administratiu = fields.Boolean()

    years = fields.Integer(compute="_get_calculEdad") 
    presu_pacient = fields.One2many(comodel_name='sale.order', inverse_name="partner_id" ) 
    #relacions
    pacient_historia = fields.Many2one('gestiocliniquesdentals.historia_medica')
    pacient_entrada = fields.One2many(comodel_name='gestiocliniquesdentals.entrada', inverse_name="entrada_pacient")
    pacient_anamnesis = fields.One2many(comodel_name='gestiocliniquesdentals.anamnesis', inverse_name="anamnesis_pacient")

    pacient_cita = fields.One2many(comodel_name='gestiocliniquesdentals.cita', inverse_name="cita_pacient")
    pacient_agenda = fields.One2many(comodel_name='gestiocliniquesdentals.agenda', inverse_name="pacient_agenda")
    
    #related
    pacient_historia_id = fields.Integer(related='pacient_historia.id_historia', store=False, readonly=False)
                                                         
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
    
    def nova_hc(self):
        for t in self:
            nhistoria = self.env['gestiocliniquesdentals.historia_medica'].create({})
            t.pacient_historia = nhistoria.id
            
            return {
            'type': 'ir.actions.act_window',
            'res_model': 'gestiocliniquesdentals.historia_medica',
            'res_id': nhistoria.id,
            'view_mode': 'form',
            'target': 'current',
        }

       




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

    #dades profesionals
    categoria = fields.Selection([("1","Doctor"), ("2","Higienista"), ("3","Auxiliar"), ("4","Director"), ("5","Subdirector"), ("6","Administratiu"), ("7","Altres")])
    num_colegiat = fields.Char()
    especialitat = fields.Selection([("1", "General"), ("2", "Cirujia"), ("3", "Ortodoncia"), ("4", "Odontopediatra"), ("5","Estética")])

    #relacions

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



#***** DOCUMENTS MÉDICS ****************************************************************

class historia_medica(models.Model):
    _name = 'gestiocliniquesdentals.historia_medica'
    _description = 'Informació mèdica del pacient'

    #personal dates
    id_historia = fields.Integer(readonly=False)

    data_alta = fields.Date()
    descripcio = fields.Text()

    #relacions
    historia_entrada = fields.Many2many(comodel_name='gestiocliniquesdentals.entrada', relation="historia_entrada")
    historia_pacient = fields.Many2one('res.partner', compute="_get_pacient")

    #funcions
    def _get_pacient(self):
        for r in self:
            historia_pacient = self.env['res.partner'].search([('pacient_historia.id','=',r.id)])
            print(historia_pacient)
            if len(historia_pacient) > 0:
                r.historia_pacient = historia_pacient[0].id
            else:
                r.historia_pacient = False


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
    entrada_historia = fields.Many2many(comodel_name='gestiocliniquesdentals.historia_medica', relation="historia_entrada")
    entrada_pacient = fields.Many2one(comodel_name='res.partner')    

class anamnesis(models.Model):
    _name = 'gestiocliniquesdentals.anamnesis'
    _description = 'anamnesis del pacient'

    #personal dates
    id_anamnesis = fields.Char()
    data_alta_anam = fields.Date()
    notes = fields.Char()
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
    publish_date = fields.Datetime('Publish date')
    #relacions
    agenda_cites = fields.Many2one(comodel_name='gestiocliniquesdentals.cita')
    # agenda_pacient = fields.Many2one(comodel_name='res.partner')

    pacient_agenda = fields.Many2one(comodel_name='res.partner')
    tractament = fields.Many2one(comodel_name='product.product')

    #related
    descripcio_curta_cita_agenda = fields.Char(related='agenda_cites.descripcio_curta_cita', store=False, readonly=False)
    # descripcio_llarga_cita_agenda = fields.Char(related='agenda_cites.descripcio_llarga_cita', store=False, readonly=False)
    descripcio_llarga_cita_agenda = fields.Char()

class cita(models.Model):
    _name = 'gestiocliniquesdentals.cita'
    _description = 'cites de la agenda i del usuari en concret'

    #personal dates
    name = fields.Char()
    id_cita = fields.Integer()
    publish_date = fields.Datetime('Publish date')
    descripcio_curta_cita = fields.Char()
    descripcio_llarga_cita = fields.Char()

    #relacions
    cita_agenda  = fields.One2many(comodel_name='gestiocliniquesdentals.agenda', inverse_name="agenda_cites")
    cita_pacient = fields.Many2one(comodel_name='res.partner')

#***** TRACTAMENTS I PRODUCTES *********************************************************

class tractament(models.Model):
    _name = 'product.product'
    _inherit = 'product.product'

    _description = 'Tractaments que es realitzen en la clínica'

    #personal dates
    temps_estimat_duracio = fields.Integer()
    compost = fields.Boolean()
    categoria_tractament = fields.Selection([("1", "General"), ("2", "Cirujia"), ("3", "Ortodoncia"), ("4", "Odontopediatra"), ("5","Estética"), ("6","Altres")])

    #relacions


        

class presupost(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    _description = 'Presupostos que es realitzen als pacients'

    
    #personal
    categoria = fields.Char()
    #relations

    



class linies_presupost_tractament(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    _description = 'Tractaments que es realitzen en la clínica que es detallen en el presupost'

    #personal dates
    namberone = fields.Char()
    num_pesa = fields.Integer()

    #relacions


