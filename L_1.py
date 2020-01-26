import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


LOS, OK, A, B, C, D, E, EE, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, AA, BB, CC, DD, FF, GG, HH, II, ORT, PHOTO = range(39)


TEXT1 = '''Hallo. Ich bin ein Mediationsbot. \nIch werde euch einige Fragen stellen. Schickt mir bitte nach euren Antworten einen Sticker, um zur nächsten Frage überzugehen.
Bitte stellt euch kurz vor. Wie heißt ihr?'''

TEXTA = ''' Ich kann euch bei eurem Konflikt eine Hilfestellung geben.
Ich werde euch durch einen strukturierten Ablauf führen um am Ende möglicherweise eine Lösung für euren Konflikt zu finden.
Mir geht es aber nicht darum, dass ihr euch einigt.
Sondern dass ihr eine Entscheidung treffen könnt, ob ihr euch überhaupt einigen wollt und wenn ja, unter welchen Umständen das möglich ist.
Ich bin nur zuständig für den Prozess, nicht für das Ergebnis.
Ihr seid beide individuell komplexe, lebendige Menschen und somit die Experten eures Konflikts.
Ich kann den Konflikt für euch nicht entscheiden, die Kontrolle über den Ausgang des Prozesses bleibt bei euch.\n
Bitte sendet einen Sticker, um fortzufahren.

                           '''
TEXTB ='''Um die Mediation zu beginnen, ist es wichtig, eine erste Grundvereinbarung zu treffen:
Dieser Chat ist ein geschützter Raum, was wir hier besprechen ist vertraulich und soll den chat nicht verlassen. 
Diese Gewissheit ermöglicht euch beiden auch, in einer größeren Offenheit miteinander zu sprechen.
Bitte verpflichtet euch, Antworten genau zu lesen oder anzuhören und keine verletzende Ausdrucksweise zu verwenden.
Versucht, euch während dem Chatverlauf an einem ruhigen Ort aufzuhalten, in dem ihr euch wohlfühlt.\n
Der Chat ist freiwillig. Ihr könnt ihn jederzeit verlassen.
Bitte sendet einen Sticker, um fortzufahren.
'''


TEXTG ='''Bitte schildert nun eure Sicht des Konflikts.
Worum geht es genau, wie steht ihr zueinander?
'''

TEXTH ='''Wie fühlst du dich, wenn du an den Konflikt denkst?
Wie sehr belastet er dich'''

TEXTI ='''Wieviel Aufmerksamkeit und Zeit investiert ihr in den Konflikt?'''

TEXTJ ='''Ist euch eure Beziehung überhaupt noch wichtig?'''

TEXTK ='''Welches Verhalten des anderen wird zum Problem für euch?
Warum nehmt ihr es als problematisch wahr?'''

TEXTL ='''Angenommen, ihr habt auf das Verhalten Anderer nur einen geringen Einfluss, wo würdet ihr dann nach einer Lösung suchen?'''

TEXTM ='''Was könnte euer Anteil an der problematischen Situation sein?
Welche dieser Gefühle habt ihr am besten im Griff und könntet es vielleicht selbst beeinflussen?'''

TEXTN ='''Sucht euch eine Situation aus, die eurer Beziehung entspricht.
Was denkst du über die verschiedenen Rollen, was wird dabei dargestellt?\n
Beschribt diese Rollenverteilung bitte mit einer Sprachnachricht.'''



TEXTO ='''Wähle nun ein Modell, mit dem du zufriedener bist.
Welches Modell entspricht deiner Lösungsvorstellung am
ehesten?\n
Was verändert sich, wenn sich die Positionen verändern?'''

TEXTP='''Benennt 3 für euch entscheidende Situation im Verlauf des Konflikts.
Nehmt ein Seil und versucht den Konfliktverlauf mit in einer Linie im Raum auszulegen.
Der Anfangspunkt der Linie stellt den Beginn des Konflikts dar, der Endpunkt den heutigen Tag.'''

TEXTQ ='''Sucht euch nun 3 Objekte in eurer Reichweite und ordnet
jedes einer der 3 Situationen zu.
Legt die Objekte auf die Linie, der Standpunkt symbolisiert
ihren Zeitpunkt im Konfliktverlauf.'''

TEXTR='''Nehmt ein Foto davon auf und schickt es in den Chat.
'''


TEXTS='''Lauft nun entgegen des Zeitverlaufs von Objekt zu Objekt in Richtung Anfangspunkt und haltet bei jedem Objekt kurz inne.
Filmt eure Füße dabei und beschreibt bei jedem Objekt, welche Gefühle ihr mit der Situation verbindet.
Schickt das Video in den Chat.'''

TEXTT='''Erinnert euch nun an 3 Situationen im Verlauf des Konflikts, an denen ihr euch besonders frei und entspannt gefühlt habt. Sucht wieder 3 symbolische Objekte in eurer Reichweite und lege sie aus.
(Lauft nun vom Anfangspunkt wieder zurück in Richtung des heutigen Punktes und beschreibe auch hier bei jedem Punkt eure Gefühle.)'''

TEXTU='''Hat euch an den gehörten Schilderungen etwas überrascht?
Verändert sich dadurch eure Sicht auf den Konflikt?'''

TEXTV='''Sucht euch nun einen Punkt in der Zukunft, an dem der Konflikt in eurem Sinne gelöst ist.
Von der Lösung aus betrachtet fühlt sich ein Konflikt manchmal ganz klein an. Geht zu diesem Punkt und blickt zurück auf die Objekte und schicke ein Foto davon in den Chat.
Beginnt nun von diesem Punkt aus, alle Objekte wieder langsam einzusammeln.'''

TEXTW='''Jetzt, wo ihr eure Gefühle gehört habt, was denkt ihr darüber?
Wenn ihr etwas noch nicht verstanden habt, was sollte noch einmal erklärt werden?'''

TEXTX='''Sucht nun jeweils ein Foto in eurer Smartphonemediathek, auf dem ihr beide zusammen seid.
Jedes Bild erzählt eine Geschichte, von dem Moment, in dem es aufgenommen wurde und der damaligen Beziehungssituation.
Bitte schickt es in den Chat.'''

TEXTY='''Bitte beschreibt den Moment der Aufnahme:
Wo und wann ist es entstanden, wer ist alles darauf zu sehen?
Was würden die Personen auf dem Bild über euch erzählen? Was hat sich seitdem verändert?
Unter welchen Umständen könnte die Situation heute wieder hergestellt werden, was müsstet ihr dafür tun?'''

TEXTZ='''Nun haben wir schon einiges besprochen.
Ich bitte euch, den bisherigen Chat wieder bis zum Anfang hochzuscrollen und ihn nocheinmal durchzulesen. Nehmt euch dafür genügend Zeit.\n
 Seid ihr einverstanden, wenn wir uns in 30 Minuten wieder hier unten treffen?'''

TEXTAA='''Nun da ihr alles nocheinmal reflektieren konntet:
Was wünscht ihr euch von der anderen Seite?
Wie soll euer Verhältnis in Zukunft aussehen?'''

TEXTBB='''Was würdet ihr ohne den Konflikt machen?'''

TEXTCC='''Nun könnt ihr ganz frei überlegen, wie ihr diese Form von Verhältnis herbeiführen könntet.
Ihr könnt alles aufzählen, was euch dazu einfällt.
Nicht jede Option muss realistisch oder durchführbar sein.'''

TEXTDD='''Welcher Vorschlag entspricht am ehesten euren Kriterien für eine gute Lösung, die ihr anfangs ausgewählt habt?'''

TEXTFF='''Wie realistisch ist das?'''

TEXTGG='''Seid ihr damit einverstanden?'''

TEXTHH='''Ich bitte euch nun, gemeinsam eine Vereinbarung zu formulieren. \n
Falls ihr einverstanden seid, empfehle ich euch, dies in einem gemeinsamen Telefonat oder persönlichen Treffen zu tun.'''

TEXTII='''Jetzt ist es Zeit, mich aus dem Chat zu verabschieden.
Ich danke euch für eure Bereitschaft und Offenheit.
Danke für euer Vertrauen in mich.'''




def start(update, context):
    update.message.reply_text(TEXT1)

    return B


def b(update, context):

    update.message.reply_text('wie alt seid ihr?')

    return C





def c(update, context):
    update.message.reply_text('In welcher Beziehung steht ihr zueinander?')

    return D



num_users = 2
stickers_sent = {}

def d(update, context):
    if not update.effective_user.is_bot:
        stickers_sent[update.effective_user.id] = True

    if len(stickers_sent) == num_users:
        update.message.reply_text('Wie geht es euch heute?')
        stickers_sent = {}
        return E
    else:
        return E

def d(update, context):
    update.message.reply_text('Wie geht es euch heute?')

    return E

def e(update, context):

    update.message.reply_text('Habt ihr gerade Zeit?')

    return EE



def ee(update, context):

    update.message.reply_text(TEXTA )

    return F



def f(update, context):

    update.message.reply_text(TEXTB)

    return LOS



def los(update, context):
    reply_keyboard = [['ja', 'nein']]

    update.message.reply_text('Bist du mit der Mediation einverstanden?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return OK





def ok(update, context):

    update.message.reply_text('''
    Bei einem Konflikt kommen meist viele verschiedene Faktoren zusammen, aber vielleicht können wir schon ein Ziel für diese Mediation finden.
Was erhofft ihr euch von diesem Chat?
Was genau soll sich nach der Mediation verändert haben?''',
        reply_markup=ReplyKeyboardRemove())


    return ORT


def ort(update, context):

    update.message.reply_text('Wo seid ihr gerade? Bitte nehmt ein Foto von dem Ort auf, an dem ihr euch befindet und postet es in den Chat.'
                              'oder sende /skip wenn du das nicht willst')

    return PHOTO







def photo(update, context):

    update.message.reply_text('Danke.'
                              )


    return G





def skip_photo(update, context):

    update.message.reply_text('in Ordnung')

    return G



def g(update, context):

    update.message.reply_text(TEXTG
                              )

    return H



def h(update, context):

    update.message.reply_text(TEXTH)

    return I


def i(update, context):

    update.message.reply_text(TEXTI)

    return J

def j(update, context):

    update.message.reply_text(TEXTJ)

    return K

def k(update, context):

    update.message.reply_text(TEXTK)

    return L

def l(update, context):

    update.message.reply_text(TEXTL)

    return M

def m(update, context):

    update.message.reply_text(TEXTM)

    return N

def n(update, context):

    update.message.reply_text(TEXTN)

    return O

def o(update, context):

    update.message.reply_text(TEXTO)

    return P

def p(update, context):

    update.message.reply_text(TEXTP)

    return Q

def q(update, context):

    update.message.reply_text(TEXTQ)


    return R

def r(update, context):

    update.message.reply_text(TEXTR)

    return S

def s(update, context):

    update.message.reply_text(TEXTS)

    return T

def t(update, context):

    update.message.reply_text(TEXTT)

    return U

def u(update, context):

    update.message.reply_text(TEXTU)

    return V

def v(update, context):

    update.message.reply_text(TEXTV)

    return W

def w(update, context):

    update.message.reply_text(TEXTW)

    return X

def x(update, context):

    update.message.reply_text(TEXTX)

    return Y

def y(update, context):

    update.message.reply_text(TEXTY)

    return Z

def z(update, context):

    update.message.reply_text(TEXTZ)

    return AA




def aa(update, context):

    update.message.reply_text(TEXTAA)

    return BB

def bb(update, context):

    update.message.reply_text(TEXTBB)

    return CC

def cc(update, context):

    update.message.reply_text(TEXTDD)

    return DD

def dd(update, context):

    update.message.reply_text(TEXTDD)

    return FF

def ff(update, context):

    update.message.reply_text(TEXTFF)

    return GG

def gg(update, context):

    update.message.reply_text(TEXTGG)

    return HH

def hh(update, context):

    update.message.reply_text(TEXTHH)

    return II

def ii(update, context):

    update.message.reply_text(TEXTII)

    return A




def audio(update, context):

    update.message.reply_text(TEXTN)

    return A




def end(update, context):

    update.message.reply_text('In welcher Beziehung steht ihr zueinander?')

    return ConversationHandler.END




def cancel(update, context):

    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END





def main():

    updater = Updater("836079024:AAEDt3Tc8qFuzJ3OW2K_foyTr8vfEP-9JV8", use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={

            OK: [MessageHandler(Filters.regex('^(ja|nein)$'), ok)],

            PHOTO: [MessageHandler(Filters.photo, photo),
                    CommandHandler('skip', skip_photo)],
            LOS: [MessageHandler(Filters.sticker, los)],

            B: [MessageHandler(Filters.sticker, b)],
            C: [MessageHandler(Filters.sticker, c)],
            D: [MessageHandler(Filters.sticker, d)],
            E: [MessageHandler(Filters.sticker, e)],
            EE: [MessageHandler(Filters.sticker, ee)],
            F: [MessageHandler(Filters.sticker, f)],
            G: [MessageHandler(Filters.sticker, g)],
            H: [MessageHandler(Filters.sticker, h)],
            I: [MessageHandler(Filters.sticker, i)],
            J: [MessageHandler(Filters.sticker, j)],
            K: [MessageHandler(Filters.sticker, k)],
            L: [MessageHandler(Filters.sticker, l)],
            M: [MessageHandler(Filters.sticker, m)],
            N: [MessageHandler(Filters.sticker, n)],
            O: [MessageHandler(Filters.sticker, o)],
            P: [MessageHandler(Filters.sticker, p)],
            Q: [MessageHandler(Filters.sticker, q)],
            R: [MessageHandler(Filters.sticker, r)],
            S: [MessageHandler(Filters.sticker, s)],
            T: [MessageHandler(Filters.sticker, t)],
            U: [MessageHandler(Filters.sticker, u)],
            V: [MessageHandler(Filters.sticker, v)],
            W: [MessageHandler(Filters.sticker, w)],
            X: [MessageHandler(Filters.sticker, x)],
            Y: [MessageHandler(Filters.sticker, y)],
            Z: [MessageHandler(Filters.sticker, z)],
            AA: [MessageHandler(Filters.sticker, aa)],
            BB: [MessageHandler(Filters.sticker, bb)],
            CC: [MessageHandler(Filters.sticker, cc)],
            DD: [MessageHandler(Filters.sticker, dd)],
            FF: [MessageHandler(Filters.sticker, ff)],
            GG: [MessageHandler(Filters.sticker, gg)],
            HH: [MessageHandler(Filters.sticker, hh)],
            II: [MessageHandler(Filters.sticker, ii)],

            ORT: [MessageHandler(Filters.sticker, ort)],

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)


    updater.start_polling()


    updater.idle()


if __name__ == '__main__':
    main()