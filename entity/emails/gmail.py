from imbox import Imbox
import config


class Gmail():
    def __init__(self):
        self.name = 'GMAIL'
        self.host = 'imap.gmail.com'
        self.email = config.GMAIL_EMAIL
        self.password = config.GMAIL_APP
        self.black_list = [
            'recommendations@discover.pinterest.com',
            'recommendations@explore.pinterest.com',
            'recommendations@ideas.pinterest.com',
            'pinterest-recommendations@ideas.pinterest.com',
            'news@emkt.cvc.com.br',
            'novidades@promo.cvc.com.br',
            'bebee@hive.bebee.com',
            'tokstok@i.tokstok.com.br',
            'giovanna@lucatelli.consultorialucatelli.com.br',
            'no-reply@zoom.us',
            'alert@notification.bebee.com',
            'voegol@news.voegol.com.br',
            'tagitau.ofertas@itau.com.br',
            'premium@academia-mail.com',
            'alertas+d@emails.decolar.com',
            'sapo@mkt.sapo.pt',
            'team@e.miro.com',
            'Você vai AMAR o meu novo Original - promo@lookemail.com.br',
            'contato@e.drogasil.com.br',
            'newsletter@mail.bubble.io'
            ]
        self.not_important = [
            'admissions@quantic.edu',
            'news@accounts.studyportalsmail.com',
            'noreply@medium.com',
            'nytdirect@nytimes.com',
            'notifications@landing.jobs',
            'jobalerts-noreply@linkedin.com',
            'marketing@go08.informamarkets.com',
            'noreply@oracle.com',
            'comunicacaodigital@itaupersonnalite.com.br',
            'mailer@jobleads.com',
            'sitesantander@santander.com.br',
            'enase@go08.informamarkets.com',
            'flavio@mail.flaviocopes.com',
            'webservice@hydrogenfuelnews.com',
            'itau-empresas@itau.com.br',
            'contact@thevirtualinstructor.com',
            'eric.beck@email.jobleads.com',
            'team@learn.mail.monday.com',
            'mission-hydrogen@mission-hydrogen.de',
            'hello@levels.fyi',
            'newsletters-noreply@linkedin.com',
            'news@geekwire.com',
            'interdtvm@comunicacao.inter.co',
            'team@hello.jobscan.co',
            'info@members.netflix.com',
            'Dell_Technologies@br.home.dell.com',
            'azul@news-voeazul.com.br',
            'lenovo@ecomm.lenovo.com',
            'job@neuvoo.com',
            'webmaster@canalenergia.com.br',
            'no-reply@jobs.reed.co.uk',
            'admissions@em.nu.edu',
            'alert@indeed.com',
            'daily@updates.miro.com',
            'noreply@jobillico.com',
            'vfe-campaign-response@amazon.com.br',
            'blog@hubspot.com',
            'clickbus@e.mailclickbus.com',
            'mary.lander@landing.jobs'
        ]

    def get_emails(self):
        with Imbox(self.host, username=self.email, password=self.password) as imbox:
            messages = imbox.messages(unread=True)

            for uid, message in messages:
                #print(f"De: {message.sent_from}")

                if message.sent_from[0]['email'] in self.black_list:
                    print(f'Deleting {message.subject}')
                    imbox.delete(uid)

                if message.sent_from[0]['email'] not in self.not_important:
                    print(f'{message.subject} - {message.sent_from[0]["email"]}')                
                #print(f"Corpo do Email: {message.body['plain']}")'
