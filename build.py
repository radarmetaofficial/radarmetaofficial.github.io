"""Genera la web de Publicador Videos (ES en la raíz, EN en en/) a partir de los textos de este archivo.

Uso:  python build.py
Crea index.html, privacidad.html, condiciones.html, en/index.html, en/privacy.html y en/terms.html.
"""

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTACTO = "radarmeta.official@gmail.com"
ACTUALIZADO = {"es": "24 de octubre de 2026", "en": "24 October 2026"}
CUENTAS = "@unporquecadadia, @radarmeta / @radar.meta, @gym_conciencia / @gym.conciencia"

PAGES = {
    "es": {"home": "index.html", "privacy": "privacidad.html", "terms": "condiciones.html", "other": "en/index.html",
           "other_privacy": "en/privacy.html", "other_terms": "en/terms.html", "prefix": ""},
    "en": {"home": "en/index.html", "privacy": "en/privacy.html", "terms": "en/terms.html", "other": "index.html",
           "other_privacy": "privacidad.html", "other_terms": "condiciones.html", "prefix": "../"},
}

T = {
    "es": {
        "lang_name": "English", "home_link": "Inicio", "privacy": "Privacidad", "terms": "Condiciones",
        "title": "Publicador Videos",
        "desc": "Herramienta personal que lleva los vídeos terminados de tres marcas a Instagram, TikTok y YouTube Shorts.",
        "h1": "Publicador",
        "lede": "Lleva cada vídeo terminado desde su carpeta hasta Instagram, TikTok y YouTube Shorts. Lo usa una sola persona, para sus propias cuentas.",
        "tabs": ["Cómo funciona", "Las marcas", "Datos", "Preguntas", "Contacto"],
        "front_text": "Cada vídeo vive en su carpeta, con el vídeo y su descripción. Publicador la lee y la sube a la red que toca.",
        "front_btn": "Ver cómo funciona",
        "reels": [("008", "008-por-que-odias-tu-voz/"), ("010", "010-por-que-estornudas-al-sol/"),
                  ("012", "012-por-que-el-cafe-te-da…/"), ("014", "014-por-que-la-bateria…/")],
        "reel_alt": "Fotograma del vídeo {n} de @unporquecadadia",
        "how_label": "Fase del proceso",
        "stages": [
            {"name": "Carpeta", "title": "Primero, la carpeta del vídeo",
             "text": "Cuando un vídeo está terminado y revisado, queda en su propia carpeta con dos archivos: el vídeo y el texto que lo acompaña.",
             "term": "<span class=p>PS&gt;</span> ls publicar\\014-por-que-la-bateria-pasa-del-20-al-1\n\n  video.mp4         21,3 MB   1080 × 1920\n  descripcion.txt   684 caracteres\n"},
            {"name": "En seco", "title": "Después, una prueba en seco",
             "text": "Antes de subir nada, Publicador comprueba la cuenta, el vídeo y la descripción. Si algo no cumple las normas de la red, se para aquí.",
             "term": "<span class=p>PS&gt;</span> python scripts\\instagram.py subir unporquecadadia publicar\\014-…\n\n@unporquecadadia ← video.mp4 (21.3 MB), descripción de 684 caracteres\n<span class=dim>Prueba en seco: no se ha subido nada. Añade --publicar para publicarlo de verdad.</span>\n"},
            {"name": "Publicación", "title": "Luego, la publicación revisada",
             "text": "Solo con la orden explícita de publicar se sube el vídeo. Instagram y YouTube lo procesan y lo publican en la cuenta de su marca.",
             "term": "<span class=p>PS&gt;</span> python scripts\\instagram.py subir unporquecadadia publicar\\014-… --publicar\n\nSubiendo el vídeo…\n<span class=ok>Publicado en @unporquecadadia</span>\n"},
            {"name": "Borrador", "title": "Y en TikTok, un borrador",
             "text": "En TikTok el vídeo llega como borrador a la bandeja de la cuenta. La publicación final se hace a mano, desde la app.",
             "term": "<span class=p>PS&gt;</span> python scripts\\tiktok.py subir gym.conciencia publicar\\…\n\n<span class=ok>Enviado a los borradores de @gym.conciencia</span>\n<span class=dim>Ábrelo en la app de TikTok para revisarlo y publicarlo.</span>\n"},
        ],
        "brands_h": "Tres marcas",
        "brands": {
            "unporquecadadia": {"name": "Un Porqué Cada Día", "img": "img/unporquecadadia.webp", "colour": "#FF7A2F",
                                "alt": "Logo de Un Porqué Cada Día: una interrogación naranja con un anillo",
                                "fact": "<strong>Curiosidades con ciencia, en un minuto.</strong><ul class=tabs-list><li>Instagram @unporquecadadia</li><li>TikTok @unporquecadadia</li><li>YouTube @unporquecadadia</li></ul>"},
            "radarmeta": {"name": "RadarMeta", "img": "img/radarmeta.webp", "colour": "#1E4874",
                          "alt": "Logo de RadarMeta: las letras RM dentro de un anillo",
                          "fact": "<strong>Cada parche de League of Legends, explicado con datos.</strong><ul class=tabs-list><li>Instagram @radarmeta</li><li>TikTok @radar.meta</li><li>YouTube @RadarMeta</li></ul>"},
            "gym_conciencia": {"name": "Gym con Ciencia", "img": "img/gym_conciencia.webp", "colour": "#0A2140",
                               "alt": "Logo de Gym con Ciencia: Álex, el entrenador dibujado, con un aro naranja",
                               "fact": "<strong>Mitos del gimnasio, desmontados con estudios.</strong><ul class=tabs-list><li>Instagram @gym_conciencia</li><li>TikTok @gym.conciencia</li><li>YouTube @gym_conciencia</li></ul>"},
        },
        "data_word": "Datos",
        "data_intro": "Publicador no tiene servidor ni base de datos en internet. Todo lo que guarda está en el ordenador de quien lo usa.",
        "data_bars": [
            ("Llaves de acceso", [("Instagram", "60 días, renovables"), ("TikTok", "24 h; renovación, 1 año"), ("YouTube", "Hasta que se retire el permiso"), ("Dónde", "Solo en el ordenador")]),
            ("Identidad de la cuenta", [("ID de usuario o de canal", "Para saber a qué cuenta subir"), ("Nombre de usuario", "Para comprobarla"), ("Foto y nombre visible (TikTok)", "Solo se muestran, no se guardan")]),
            ("Vídeos y descripciones", [("Origen", "Carpeta publicar/ del propio proyecto"), ("Destino", "Solo la cuenta de su marca"), ("Copia en la herramienta", "Ninguna")]),
            ("Registros", [("Renovación de llaves", "Fecha y «OK» por cuenta"), ("Dónde", "Solo en el ordenador")]),
            ("Lo que no se recoge", [("Seguidores, mensajes, comentarios", "Nunca"), ("Datos de otras personas", "Nunca"), ("Venta o cesión de datos", "Nunca")]),
            ("Esta web", [("Cookies", "Ninguna"), ("Analítica o rastreo", "Ninguno"), ("Fuentes y archivos", "Alojados aquí mismo")]),
        ],
        "faq_h": "Preguntas",
        "faq": [
            ("¿Qué es Publicador Videos?", ["Una herramienta personal, sin interfaz pública, que sube los vídeos ya terminados de tres marcas a sus propias cuentas de Instagram, TikTok y YouTube."]),
            ("¿Puede usarla otra persona?", ["No. No hay registro ni usuarios externos: solo funciona con las cuentas de sus marcas, que han dado permiso expresamente."]),
            ("¿Publica algo sin que se revise?", ["No. Cada vídeo se revisa antes y solo se publica con una orden explícita. En TikTok ni siquiera eso: llega como borrador y se publica a mano desde la app."]),
            ("¿Dónde se guardan las llaves de acceso?", ["En el ordenador de quien la usa, en una carpeta fuera de cualquier proyecto o repositorio. Nunca se suben a internet ni se publican."]),
            ("¿Guarda datos de otras personas?", ["No. Solo trata datos de las propias cuentas: su identificador, su nombre de usuario y las llaves de acceso."]),
            ("¿Qué permisos pide en cada red?", ["Instagram: leer el perfil básico y publicar contenido. TikTok: leer el perfil básico y enviar vídeos a borradores. YouTube: subir vídeos al canal."]),
            ("¿Cómo se desconecta una cuenta?", ["Desde cada red se puede retirar el permiso en cualquier momento; la página de privacidad explica dónde. Al retirarlo, la llave deja de funcionar al instante."]),
            ("¿Usa cookies esta web?", ["No. Ni cookies, ni analítica, ni fuentes o scripts de terceros. Todo lo que ves se sirve desde aquí."]),
        ],
        "c_h": "Escribe al responsable",
        "c_p": "Para preguntas sobre la herramienta, los datos o retirar un permiso. Se abrirá tu programa de correo con el mensaje preparado.",
        "c_name": "Tu nombre", "c_email": "Tu correo", "c_topic": "Tema",
        "c_topics": ["Privacidad o datos", "Retirar un permiso", "Otra consulta"],
        "c_msg": "Tu mensaje", "c_send": "Preparar el correo", "c_subject": "Publicador Videos",
        "f_tool": "Herramienta", "f_legal": "Legal", "f_brands": "Marcas", "f_lang": "Idioma",
        "f_top": "Volver arriba", "f_note": "Herramienta personal · sin cookies",
        "f_how": "Cómo funciona", "f_faq": "Preguntas",
    },
    "en": {
        "lang_name": "Español", "home_link": "Home", "privacy": "Privacy", "terms": "Terms",
        "title": "Publicador Videos",
        "desc": "A personal tool that takes three brands' finished videos to Instagram, TikTok and YouTube Shorts.",
        "h1": "Publicador",
        "lede": "It takes each finished video from its folder to Instagram, TikTok and YouTube Shorts. One person uses it, for their own accounts only.",
        "tabs": ["How it works", "The brands", "Data", "Questions", "Contact"],
        "front_text": "Every video lives in its own folder, with the video and its caption. Publicador reads it and uploads it to the right network.",
        "front_btn": "See how it works",
        "reels": [("008", "008-por-que-odias-tu-voz/"), ("010", "010-por-que-estornudas-al-sol/"),
                  ("012", "012-por-que-el-cafe-te-da…/"), ("014", "014-por-que-la-bateria…/")],
        "reel_alt": "Frame from video {n} by @unporquecadadia",
        "how_label": "Stage of the process",
        "stages": [
            {"name": "Folder", "title": "First, the video's folder",
             "text": "Once a video is finished and reviewed, it sits in its own folder with two files: the video and the caption that goes with it.",
             "term": "<span class=p>PS&gt;</span> ls publicar\\014-por-que-la-bateria-pasa-del-20-al-1\n\n  video.mp4         21.3 MB   1080 × 1920\n  descripcion.txt   684 characters\n"},
            {"name": "Dry run", "title": "Then, a dry run",
             "text": "Before anything is uploaded, Publicador checks the account, the video and the caption. If something breaks the network's rules, it stops here.",
             "term": "<span class=p>PS&gt;</span> python scripts\\instagram.py subir unporquecadadia publicar\\014-…\n\n@unporquecadadia ← video.mp4 (21.3 MB), descripción de 684 caracteres\n<span class=dim>Prueba en seco: no se ha subido nada. Añade --publicar para publicarlo de verdad.</span>\n"},
            {"name": "Publish", "title": "Next, the reviewed post",
             "text": "The video is only uploaded with an explicit publish command. Instagram and YouTube process it and post it on that brand's account.",
             "term": "<span class=p>PS&gt;</span> python scripts\\instagram.py subir unporquecadadia publicar\\014-… --publicar\n\nSubiendo el vídeo…\n<span class=ok>Publicado en @unporquecadadia</span>\n"},
            {"name": "Draft", "title": "And on TikTok, a draft",
             "text": "On TikTok the video arrives as a draft in the account's inbox. The final post is made by hand, in the app.",
             "term": "<span class=p>PS&gt;</span> python scripts\\tiktok.py subir gym.conciencia publicar\\…\n\n<span class=ok>Enviado a los borradores de @gym.conciencia</span>\n<span class=dim>Ábrelo en la app de TikTok para revisarlo y publicarlo.</span>\n"},
        ],
        "brands_h": "Three brands",
        "brands": {
            "unporquecadadia": {"name": "Un Porqué Cada Día", "img": "img/unporquecadadia.webp", "colour": "#FF7A2F",
                                "alt": "Un Porqué Cada Día logo: an orange question mark inside a ring",
                                "fact": "<strong>Everyday science questions, in one minute.</strong><ul class=tabs-list><li>Instagram @unporquecadadia</li><li>TikTok @unporquecadadia</li><li>YouTube @unporquecadadia</li></ul>"},
            "radarmeta": {"name": "RadarMeta", "img": "img/radarmeta.webp", "colour": "#1E4874",
                          "alt": "RadarMeta logo: the letters RM inside a ring",
                          "fact": "<strong>Every League of Legends patch, explained with data.</strong><ul class=tabs-list><li>Instagram @radarmeta</li><li>TikTok @radar.meta</li><li>YouTube @RadarMeta</li></ul>"},
            "gym_conciencia": {"name": "Gym con Ciencia", "img": "img/gym_conciencia.webp", "colour": "#0A2140",
                               "alt": "Gym con Ciencia logo: Álex, the drawn coach, inside an orange ring",
                               "fact": "<strong>Gym myths, taken apart with studies.</strong><ul class=tabs-list><li>Instagram @gym_conciencia</li><li>TikTok @gym.conciencia</li><li>YouTube @gym_conciencia</li></ul>"},
        },
        "data_word": "Data",
        "data_intro": "Publicador has no server and no online database. Everything it keeps is on the computer of the person who uses it.",
        "data_bars": [
            ("Access keys", [("Instagram", "60 days, renewable"), ("TikTok", "24 h; refresh, 1 year"), ("YouTube", "Until permission is revoked"), ("Where", "Only on the computer")]),
            ("Account identity", [("User or channel ID", "To know which account to post to"), ("Username", "To check it"), ("Avatar and display name (TikTok)", "Shown only, not stored")]),
            ("Videos and captions", [("Source", "The project's own publicar/ folder"), ("Destination", "Only that brand's account"), ("Copy kept by the tool", "None")]),
            ("Logs", [("Key renewals", "Date and “OK” per account"), ("Where", "Only on the computer")]),
            ("What is never collected", [("Followers, messages, comments", "Never"), ("Other people's data", "Never"), ("Selling or sharing data", "Never")]),
            ("This website", [("Cookies", "None"), ("Analytics or tracking", "None"), ("Fonts and files", "Hosted right here")]),
        ],
        "faq_h": "Questions",
        "faq": [
            ("What is Publicador Videos?", ["A personal tool, with no public interface, that uploads three brands' finished videos to their own Instagram, TikTok and YouTube accounts."]),
            ("Can anyone else use it?", ["No. There is no sign-up and there are no outside users: it only works with its brands' accounts, which have expressly granted permission."]),
            ("Does it post anything unreviewed?", ["No. Every video is reviewed first and only posted with an explicit command. On TikTok not even that: it arrives as a draft and is posted by hand in the app."]),
            ("Where are the access keys kept?", ["On the computer of the person who uses it, in a folder outside any project or repository. They are never uploaded or published."]),
            ("Does it keep other people's data?", ["No. It only handles data about its own accounts: their ID, their username and the access keys."]),
            ("Which permissions does it ask for?", ["Instagram: read the basic profile and publish content. TikTok: read the basic profile and send videos to drafts. YouTube: upload videos to the channel."]),
            ("How is an account disconnected?", ["Permission can be revoked on each network at any time; the privacy page explains where. Once revoked, the key stops working immediately."]),
            ("Does this website use cookies?", ["No. No cookies, no analytics, no third-party fonts or scripts. Everything you see is served from here."]),
        ],
        "c_h": "Write to the operator",
        "c_p": "For questions about the tool, the data, or revoking a permission. Your email app will open with the message ready.",
        "c_name": "Your name", "c_email": "Your email", "c_topic": "Topic",
        "c_topics": ["Privacy or data", "Revoke a permission", "Something else"],
        "c_msg": "Your message", "c_send": "Prepare the email", "c_subject": "Publicador Videos",
        "f_tool": "Tool", "f_legal": "Legal", "f_brands": "Brands", "f_lang": "Language",
        "f_top": "Back to top", "f_note": "Personal tool · no cookies",
        "f_how": "How it works", "f_faq": "Questions",
    },
}

# ---------- Páginas legales ----------

LEGAL = {
    ("es", "privacy"): {
        "title": "Privacidad",
        "intro": f"Qué datos trata Publicador Videos, para qué, dónde se guardan y cómo retirar el permiso. Última actualización: {ACTUALIZADO['es']}.",
        "sections": [
            ("quien", "Quién la usa y quién responde", f"""
<p>Publicador Videos es una herramienta personal. La usa una sola persona, el titular de las cuentas {CUENTAS} (en adelante, «el responsable»), para publicar sus propios vídeos en sus propias cuentas. No se ofrece a terceros y no admite usuarios externos.</p>
<p>Contacto del responsable: <a href="mailto:{CONTACTO}">{CONTACTO}</a>.</p>"""),
            ("datos", "Qué datos trata", """
<table><thead><tr><th>Red</th><th>Datos</th><th>Para qué</th></tr></thead><tbody>
<tr><td>Instagram (Meta)</td><td>ID de usuario de Instagram, nombre de usuario y llave de acceso de la cuenta.</td><td>Saber en qué cuenta publicar y publicar sus Reels con su descripción.</td></tr>
<tr><td>TikTok</td><td>open_id, nombre visible y foto de perfil (permiso <em>user.info.basic</em>); llave de acceso y de renovación.</td><td>Identificar la cuenta y enviar sus vídeos a borradores (permiso <em>video.upload</em>).</td></tr>
<tr><td>YouTube (Google)</td><td>ID y nombre del canal; llave de acceso y de renovación de OAuth.</td><td>Subir los vídeos al canal de la marca.</td></tr>
</tbody></table>
<p>Además se envían a cada red el vídeo y su descripción, que son contenido propio del responsable. La herramienta no lee seguidores, mensajes, comentarios ni estadísticas, y no trata datos de ninguna otra persona.</p>"""),
            ("donde", "Dónde se guardan y cuánto tiempo", """
<ul class="tabs-list">
<li>Todo se guarda únicamente en el ordenador del responsable, en una carpeta de su perfil de usuario fuera de cualquier proyecto o repositorio. No hay servidor, base de datos en internet ni copia en la nube.</li>
<li>Instagram: la llave dura 60 días y se renueva automáticamente cada semana mientras se use.</li>
<li>TikTok: la llave dura 24 horas y la de renovación, alrededor de un año.</li>
<li>YouTube: la llave se conserva hasta que se retire el permiso.</li>
<li>Un registro local anota la fecha de cada renovación y si fue correcta; no contiene las llaves.</li>
<li>Al retirar el permiso o dejar de usar la herramienta, los archivos se borran.</li>
</ul>"""),
            ("terceros", "Con quién se comparten", """
<p>Con nadie más que la propia red: cada dato se envía solo a la plataforma a la que pertenece (Meta, TikTok o Google) y solo para publicar en la cuenta correspondiente. No se venden, no se ceden, no se usan para publicidad y no se transfieren a otros servicios.</p>"""),
            ("retirar", "Cómo retirar el permiso", """
<ul class="tabs-list">
<li><strong>Instagram:</strong> Configuración → Aplicaciones y sitios web → Activas → Publicador Videos-IG → Eliminar.</li>
<li><strong>TikTok:</strong> Perfil → Ajustes y privacidad → Seguridad y permisos → Aplicaciones y servicios → Publicador Videos → Eliminar acceso.</li>
<li><strong>YouTube / Google:</strong> en la página de permisos de tu cuenta de Google, <a href="https://myaccount.google.com/connections">myaccount.google.com/connections</a> (o <a href="https://security.google.com/settings/security/permissions">security.google.com/settings/security/permissions</a>), elige Publicador Videos y quita el acceso.</li>
</ul>
<p>También puedes pedir que se borren los datos escribiendo al contacto de arriba; se hará en un plazo máximo de 30 días.</p>"""),
            ("plataformas", "Normas de cada plataforma", """
<p>Publicador Videos usa los Servicios API de YouTube. Al usarla se aplican las <a href="https://www.youtube.com/t/terms">Condiciones de servicio de YouTube</a> y la <a href="https://policies.google.com/privacy">Política de privacidad de Google</a>.</p>
<p>También se aplican las <a href="https://www.tiktok.com/legal/terms-of-service">Condiciones de servicio</a> y la <a href="https://www.tiktok.com/legal/privacy-policy">Política de privacidad</a> de TikTok, y las <a href="https://help.instagram.com/581066165581870">Condiciones de uso de Instagram</a> y la <a href="https://privacycenter.instagram.com/policy">Política de privacidad de Meta</a>.</p>"""),
            ("web", "Esta web", """
<p>Esta página no usa cookies, ni analítica, ni rastreo, ni fuentes, vídeos o scripts de terceros: todo se sirve desde aquí mismo. El alojamiento (GitHub Pages) puede registrar datos técnicos de las visitas, como la dirección IP, según la <a href="https://docs.github.com/es/site-policy/privacy-policies/github-general-privacy-statement">declaración de privacidad de GitHub</a>.</p>"""),
            ("derechos", "Tus derechos", f"""
<p>Si crees que la herramienta trata algún dato tuyo, puedes pedir acceso, rectificación o supresión escribiendo a <a href="mailto:{CONTACTO}">{CONTACTO}</a>. También puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es">aepd.es</a>).</p>
<p>La herramienta no está dirigida a menores y no recoge datos de menores.</p>"""),
            ("cambios", "Cambios", """
<p>Si cambia lo que trata la herramienta (por ejemplo, si algún día publica directamente en TikTok), esta página se actualizará y cambiará la fecha de arriba antes de que el cambio se aplique.</p>"""),
        ],
    },
    ("en", "privacy"): {
        "title": "Privacy",
        "intro": f"What data Publicador Videos handles, why, where it is kept and how to revoke permission. Last updated: {ACTUALIZADO['en']}.",
        "sections": [
            ("who", "Who uses it and who is responsible", f"""
<p>Publicador Videos is a personal tool. It is used by one person only, the owner of the accounts {CUENTAS} (the “operator”), to publish their own videos on their own accounts. It is not offered to anyone else and has no outside users.</p>
<p>Operator contact: <a href="mailto:{CONTACTO}">{CONTACTO}</a>.</p>"""),
            ("data", "What data it handles", """
<table><thead><tr><th>Network</th><th>Data</th><th>Purpose</th></tr></thead><tbody>
<tr><td>Instagram (Meta)</td><td>Instagram user ID, username and the account's access token.</td><td>Knowing which account to post to and publishing its Reels with their caption.</td></tr>
<tr><td>TikTok</td><td>open_id, display name and avatar (<em>user.info.basic</em> scope); access and refresh tokens.</td><td>Identifying the account and sending its videos to drafts (<em>video.upload</em> scope).</td></tr>
<tr><td>YouTube (Google)</td><td>Channel ID and title; OAuth access and refresh tokens.</td><td>Uploading videos to the brand's channel.</td></tr>
</tbody></table>
<p>Each network also receives the video and its caption, which are the operator's own content. The tool does not read followers, messages, comments or analytics, and handles no data about anyone else.</p>"""),
            ("where", "Where it is kept and for how long", """
<ul class="tabs-list">
<li>Everything is stored only on the operator's computer, in a folder of their user profile outside any project or repository. There is no server, online database or cloud copy.</li>
<li>Instagram: the token lasts 60 days and is renewed automatically every week while in use.</li>
<li>TikTok: the access token lasts 24 hours and the refresh token about a year.</li>
<li>YouTube: the token is kept until permission is revoked.</li>
<li>A local log records the date of each renewal and whether it succeeded; it contains no tokens.</li>
<li>When permission is revoked or the tool is no longer used, the files are deleted.</li>
</ul>"""),
            ("sharing", "Who it is shared with", """
<p>No one but the network itself: each piece of data is sent only to the platform it belongs to (Meta, TikTok or Google), and only to publish on the matching account. It is never sold, shared, used for advertising or transferred to other services.</p>"""),
            ("revoke", "How to revoke permission", """
<ul class="tabs-list">
<li><strong>Instagram:</strong> Settings → Apps and websites → Active → Publicador Videos-IG → Remove.</li>
<li><strong>TikTok:</strong> Profile → Settings and privacy → Security and permissions → Apps and services → Publicador Videos → Remove access.</li>
<li><strong>YouTube / Google:</strong> on your Google Account permissions page, <a href="https://myaccount.google.com/connections">myaccount.google.com/connections</a> (or <a href="https://security.google.com/settings/security/permissions">security.google.com/settings/security/permissions</a>), choose Publicador Videos and remove access.</li>
</ul>
<p>You can also ask for the data to be deleted by writing to the contact above; it will be done within 30 days.</p>"""),
            ("platforms", "Platform rules", """
<p>Publicador Videos uses YouTube API Services. By using it you agree to the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a>, and the <a href="https://policies.google.com/privacy">Google Privacy Policy</a> applies.</p>
<p>TikTok's <a href="https://www.tiktok.com/legal/terms-of-service">Terms of Service</a> and <a href="https://www.tiktok.com/legal/privacy-policy">Privacy Policy</a>, and Instagram's <a href="https://help.instagram.com/581066165581870">Terms of Use</a> and <a href="https://privacycenter.instagram.com/policy">Meta's Privacy Policy</a> also apply.</p>"""),
            ("site", "This website", """
<p>This site uses no cookies, analytics, tracking, or third-party fonts, videos or scripts: everything is served from here. The host (GitHub Pages) may log technical data about visits, such as IP addresses, under <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub's privacy statement</a>.</p>"""),
            ("rights", "Your rights", f"""
<p>If you believe the tool handles any data about you, you can request access, correction or deletion by writing to <a href="mailto:{CONTACTO}">{CONTACTO}</a>. You can also complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es">aepd.es</a>).</p>
<p>The tool is not aimed at children and collects no data about children.</p>"""),
            ("changes", "Changes", """
<p>If what the tool handles changes (for example, if it one day posts directly on TikTok), this page will be updated and the date above changed before the change takes effect.</p>"""),
        ],
    },
    ("es", "terms"): {
        "title": "Condiciones",
        "intro": f"Las reglas de uso de Publicador Videos. Última actualización: {ACTUALIZADO['es']}.",
        "sections": [
            ("objeto", "Qué es y para quién", f"""
<p>Publicador Videos es una herramienta personal que sube vídeos propios a las cuentas {CUENTAS}. Solo la usa su titular, para esas cuentas. No es un servicio abierto: no hay registro, ni cuentas de usuario, ni pagos.</p>"""),
            ("uso", "Uso permitido", """
<ul class="tabs-list">
<li>Solo se publica contenido propio, del que el titular tiene todos los derechos (vídeo, música, voz, imágenes y textos).</li>
<li>Cada vídeo se revisa antes de publicarse. En TikTok se envía a borradores y la publicación final se hace a mano en la app.</li>
<li>Se respetan las normas de cada red: las <a href="https://www.tiktok.com/community-guidelines">Normas de la comunidad de TikTok</a>, las <a href="https://help.instagram.com/477434105621119">Normas comunitarias de Instagram</a>, las <a href="https://www.youtube.com/howyoutubeworks/policies/community-guidelines/">Normas de la comunidad de YouTube</a> y las condiciones para desarrolladores de cada plataforma.</li>
<li>No se usa para spam, publicaciones masivas, suplantación ni para gestionar cuentas de terceros.</li>
</ul>"""),
            ("plataformas", "Condiciones de las plataformas", """
<p>Al usar la herramienta se aceptan las <a href="https://www.youtube.com/t/terms">Condiciones de servicio de YouTube</a>, las <a href="https://www.tiktok.com/legal/terms-of-service">Condiciones de servicio de TikTok</a> y las <a href="https://help.instagram.com/581066165581870">Condiciones de uso de Instagram</a>. Si alguna de ellas contradice estas condiciones, prevalece la de la plataforma.</p>"""),
            ("datos", "Datos", """
<p>El tratamiento de datos se explica en la <a href="privacidad.html">política de privacidad</a>.</p>"""),
            ("garantias", "Sin garantías", """
<p>La herramienta se usa tal cual. Depende de las API de terceros, que pueden cambiar o dejar de estar disponibles; si una red rechaza una publicación, la herramienta se detiene y no reintenta por su cuenta.</p>"""),
            ("cambios", "Cambios y ley aplicable", f"""
<p>Estas condiciones pueden cambiar; la fecha de arriba indica la última versión. Se rigen por la ley española. Contacto: <a href="mailto:{CONTACTO}">{CONTACTO}</a>.</p>"""),
        ],
    },
    ("en", "terms"): {
        "title": "Terms",
        "intro": f"The rules for using Publicador Videos. Last updated: {ACTUALIZADO['en']}.",
        "sections": [
            ("what", "What it is and who it is for", f"""
<p>Publicador Videos is a personal tool that uploads the owner's videos to the accounts {CUENTAS}. Only their owner uses it, for those accounts. It is not an open service: there is no sign-up, no user accounts and no payments.</p>"""),
            ("use", "Permitted use", """
<ul class="tabs-list">
<li>Only original content is published, to which the owner holds all rights (video, music, voice, images and text).</li>
<li>Every video is reviewed before it is published. On TikTok it is sent to drafts and the final post is made by hand in the app.</li>
<li>Each network's rules are followed: the <a href="https://www.tiktok.com/community-guidelines">TikTok Community Guidelines</a>, the <a href="https://help.instagram.com/477434105621119">Instagram Community Guidelines</a>, the <a href="https://www.youtube.com/howyoutubeworks/policies/community-guidelines/">YouTube Community Guidelines</a> and each platform's developer terms.</li>
<li>It is not used for spam, mass posting, impersonation or managing other people's accounts.</li>
</ul>"""),
            ("platforms", "Platform terms", """
<p>Using the tool means agreeing to the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a>, the <a href="https://www.tiktok.com/legal/terms-of-service">TikTok Terms of Service</a> and the <a href="https://help.instagram.com/581066165581870">Instagram Terms of Use</a>. Where any of them conflicts with these terms, the platform's terms prevail.</p>"""),
            ("data", "Data", """
<p>How data is handled is explained in the <a href="privacy.html">privacy policy</a>.</p>"""),
            ("warranty", "No warranty", """
<p>The tool is provided as is. It relies on third-party APIs that may change or become unavailable; if a network rejects a post, the tool stops and does not retry on its own.</p>"""),
            ("law", "Changes and governing law", f"""
<p>These terms may change; the date above shows the latest version. They are governed by Spanish law. Contact: <a href="mailto:{CONTACTO}">{CONTACTO}</a>.</p>"""),
        ],
    },
}


def e(s: str) -> str:
    return html.escape(s, quote=True)


def head(lang: str, title: str, desc: str, pre: str, alt_href: str) -> str:
    other = "en" if lang == "es" else "es"
    return f"""<!doctype html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" type="image/png" href="{pre}img/icono.png">
<link rel="alternate" hreflang="{other}" href="{alt_href}">
<link rel="preload" href="{pre}fonts/space-grotesk-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pre}assets/site.css">
<meta name="theme-color" content="#0A2140">
</head>
<body>
"""


def topbar(lang: str, pre: str, t: dict, alt_href: str, home: str) -> str:
    return f"""<header class="top">
  <a class="mark" href="{home}"><img src="{pre}img/icono.png" alt="" width="30" height="30">Publicador Videos</a>
  <nav aria-label="{e(t['f_legal'])}"><a href="{alt_href}" hreflang="{'en' if lang == 'es' else 'es'}">{t['lang_name']}</a></nav>
</header>
"""


def footer(lang: str, pre: str, t: dict, p: dict, home: str) -> str:
    letters = "PUBLICADOR"
    heights = [100, 78, 92, 64, 86, 100, 70, 94, 82, 74]
    colours = ["#FF7A2F", "#F4F1EA", "#7FA3CC", "#F4F1EA", "#FF7A2F", "#F4F1EA", "#7FA3CC", "#FF9A5C", "#F4F1EA", "#FF7A2F"]
    blocks = "".join(
        f'<span style="--b:{c};height:{h}%;--hm:{max(h - 20, 55)}%" aria-hidden="true">{ch}</span>'
        for ch, h, c in zip(letters, heights, colours)
    )
    privacy_href = p["privacy"].split("/")[-1]
    terms_href = p["terms"].split("/")[-1]
    return f"""<footer class="foot">
  <div class="blocks" role="img" aria-label="Publicador">{blocks}</div>
  <div class="foot__links">
    <div><a href="{home}#como">{t['f_how']}</a><a href="{home}#preguntas">{t['f_faq']}</a></div>
    <div><a href="{privacy_href}">{t['privacy']}</a><a href="{terms_href}">{t['terms']}</a></div>
    <div><a href="https://www.instagram.com/unporquecadadia/">Un Porqué Cada Día</a><a href="https://www.instagram.com/radarmeta/">RadarMeta</a><a href="https://www.instagram.com/gym_conciencia/">Gym con Ciencia</a></div>
    <div><a href="{'en/index.html' if lang == 'es' else '../index.html'}" hreflang="{'en' if lang == 'es' else 'es'}">{t['lang_name']}</a></div>
    <div class="contact-lines"><a href="mailto:{CONTACTO}">{CONTACTO}</a><span>{t['f_note']}</span></div>
  </div>
  <div class="foot__last"><span>© 2026 Publicador Videos</span><a class="btn btn--dark" href="#top">{t['f_top']}</a></div>
</footer>
<script src="{pre}assets/site.js"></script>
</body>
</html>
"""


def home(lang: str) -> str:
    t, p = T[lang], PAGES[lang]
    pre = p["prefix"]
    alt_href = ("en/index.html" if lang == "es" else "../index.html")
    out = [head(lang, f"{t['title']} · {t['tabs'][0]}", t["desc"], pre, alt_href), '<div id="top"></div>',
           topbar(lang, pre, t, alt_href, "index.html")]

    # Portada: pila de carpetas, una por sección; la de delante está abierta
    ids = ["como", "marcas", "datos", "preguntas", "contacto"]
    cols = [("var(--navy-3)", None), ("var(--cream)", "var(--ink-dark)"), ("var(--navy-2)", None), ("#2A5A8C", None), ("var(--accent)", "var(--ink-dark)")]
    xs = ["4%", "22%", "44%", "62%", "78%"]
    xm = ["0%", "34%", "56%", "8%", "50%"]
    folders = []
    for depth, k in enumerate(reversed(range(5))):
        c, ink = cols[k]
        style = f"--i:{depth};--c:{c};--x:{xs[k]};--xm:{xm[k]}" + (f";--t:{ink}" if ink else "")
        if k == 0:
            reels = "".join(
                f"""<figure class="reel rise" style="--d:{120 + 80 * j}ms"><div class="folder-mask">{
                    f'<video src="{pre}video/014.mp4" poster="{pre}video/014-poster.webp" autoplay muted loop playsinline width="360" height="640" aria-label="{e(t["reel_alt"].format(n=n))}"></video>' if n == "014"
                    else f'<img src="{pre}img/{n}.webp" alt="{e(t["reel_alt"].format(n=n))}" width="540" height="960">'
                }</div><figcaption>{e(cap)}</figcaption></figure>"""
                for j, (n, cap) in enumerate(t["reels"])
            )
            folders.append(f"""<div class="folder folder--front" style="{style}">
  <a class="folder__tab" href="#{ids[k]}">{t['tabs'][k]}</a>
  <div class="folder__body">
    <div class="front__lead rise"><span class="front__path">publicar/NNN-tema/</span><p>{t['front_text']}</p><a class="btn" href="#{ids[k]}">{t['front_btn']}</a></div>
    <div class="reels">{reels}</div>
  </div>
</div>""")
        else:
            folders.append(f'<a class="folder" style="{style}" href="#{ids[k]}"><span class="folder__tab">{t["tabs"][k]}</span><span class="folder__body"></span></a>')
    out.append(f"""<main>
<section class="hero">
  <div class="hero__text"><h1 class="rise">{t['h1']}</h1><p class="hero__lede rise" style="--d:90ms">{t['lede']}</p></div>
  <div class="stack">{''.join(folders)}</div>
</section>
""")

    # Cómo funciona
    s0 = t["stages"][0]
    stages_json = json.dumps(t["stages"], ensure_ascii=False).replace("</", "<\\/")
    names = "".join(f'<li class="{"on" if i == 0 else ""}"><button type="button">{e(s["name"])}</button></li>' for i, s in enumerate(t["stages"]))
    out.append(f"""<section class="how" id="como" data-how>
  <script type="application/json">{stages_json}</script>
  <div class="how__split">
    <div class="how__clause"><h2 class="rise" data-how-title>{e(s0['title'])}</h2><p class="rise" style="--d:90ms" data-how-text>{e(s0['text'])}</p></div>
    <div class="how__ui"><div class="term rise" data-ui><pre data-how-term>{s0['term']}</pre><div class="term__thumb"><div class="folder-mask"><img src="{pre}img/014.webp" alt="{e(t['reel_alt'].format(n='014'))}" width="540" height="960" loading="lazy"></div></div></div></div>
  </div>
  <div class="how__control">
    <label class="sr" for="fase">{t['how_label']}</label>
    <div class="range-wrap" data-range><span class="range-fill" aria-hidden="true"></span><input class="range" id="fase" type="range" min="0" max="{len(t['stages']) - 1}" step="1" value="0" aria-valuetext="{e(s0['name'])}"></div>
    <ol class="stages">{names}</ol>
  </div>
</section>
""")

    # Las marcas
    bjson = json.dumps({k: {**v, "img": pre + v["img"]} for k, v in t["brands"].items()}, ensure_ascii=False).replace("</", "<\\/")
    first = next(iter(t["brands"].values()))
    items = "".join(
        f'<li><button type="button" data-brand="{k}" aria-pressed="{"true" if i == 0 else "false"}">{e(v["name"])}</button></li>'
        for i, (k, v) in enumerate(t["brands"].items())
    )
    out.append(f"""<section class="brands" id="marcas" data-brands>
  <script type="application/json">{bjson}</script>
  <div class="brands__stage">
    <div class="brands__disc folder-mask" style="--bc:{first['colour']}" aria-hidden="true"></div>
    <div class="brands__obj"><img data-brand-img src="{pre}{first['img']}" alt="{e(first['alt'])}" width="640" height="640" loading="lazy"></div>
    <div class="brands__list"><h2 class="rise">{t['brands_h']}</h2><ul class="rise" style="--d:90ms">{items}</ul></div>
    <div class="brands__fact rise" style="--d:160ms" data-brand-fact aria-live="polite">{first['fact']}</div>
  </div>
</section>
""")

    # Datos
    bars = "".join(
        f"""<details class="bar rise" style="--d:{60 * i}ms"{' open' if i == 0 else ''}><summary>{e(name)}</summary><div class="bar__panel"><dl>{''.join(f'<dt>{e(a)}</dt><dd>{e(b)}</dd>' for a, b in rows)}</dl></div></details>"""
        for i, (name, rows) in enumerate(t["data_bars"])
    )
    out.append(f"""<section class="data" id="datos">
  <div class="wrap"><div class="data__col">
    <h2 class="giant rise">{t['data_word']}</h2>
    <p class="data__intro rise" style="--d:90ms">{t['data_intro']} <a href="{p['privacy'].split('/')[-1]}">{t['privacy']} →</a></p>
    {bars}
  </div></div>
</section>
""")

    # Preguntas
    tiles = "".join(
        f"""<details class="tile rise" name="faq" style="--d:{50 * i}ms"><summary>{e(q)}<span class="pm" aria-hidden="true"></span></summary><div class="tile__a">{''.join(f'<p>{e(x)}</p>' for x in a)}</div></details>"""
        for i, (q, a) in enumerate(t["faq"])
    )
    out.append(f"""<section class="faq" id="preguntas">
  <div class="wrap faq__grid"><h2 class="rise">{t['faq_h']}</h2><div>{tiles}</div></div>
</section>
""")

    # Contacto
    opts = "".join(f"<option>{e(o)}</option>" for o in t["c_topics"])
    out.append(f"""<section class="contact" id="contacto">
  <div class="wrap">
    <div class="coupon rise">
      <div class="coupon__left"><h2>{t['c_h']}</h2><p>{t['c_p']}</p></div>
      <form data-mailto="{CONTACTO}" data-subject="{e(t['c_subject'])}" action="mailto:{CONTACTO}" method="post" enctype="text/plain">
        <label class="sr" for="c-name">{t['c_name']}</label><input id="c-name" name="name" placeholder="{e(t['c_name'])}" autocomplete="name" required>
        <label class="sr" for="c-email">{t['c_email']}</label><input id="c-email" name="email" type="email" placeholder="{e(t['c_email'])}" autocomplete="email" required>
        <label class="sr" for="c-topic">{t['c_topic']}</label><select id="c-topic" name="topic">{opts}</select>
        <label class="sr" for="c-msg">{t['c_msg']}</label><textarea id="c-msg" name="message" placeholder="{e(t['c_msg'])}" required></textarea>
        <button class="btn btn--dark" type="submit">{t['c_send']}</button>
      </form>
    </div>
  </div>
</section>
</main>
""")
    out.append(footer(lang, pre, t, p, "index.html"))
    return "".join(out)


def legal(lang: str, kind: str) -> str:
    t, p = T[lang], PAGES[lang]
    pre = p["prefix"]
    d = LEGAL[(lang, kind)]
    alt_href = (p["other_privacy"] if kind == "privacy" else p["other_terms"])
    alt_href = alt_href if lang == "es" else "../" + alt_href
    toc = "".join(f'<a href="#{sid}">{e(h)}</a>' for sid, h, _ in d["sections"])
    body = "".join(f'<h2 id="{sid}">{e(h)}</h2>{content}' for sid, h, content in d["sections"])
    return "".join([
        head(lang, f"{d['title']} · Publicador Videos", d["intro"], pre, alt_href), '<div id="top"></div>',
        topbar(lang, pre, t, alt_href, "index.html"),
        f"""<main>
<section class="legal-hero"><h1 class="rise">{d['title']}</h1><p class="rise" style="--d:90ms">{d['intro']}</p></section>
<section class="legal"><div class="legal__grid"><nav class="legal__toc" aria-label="{e(d['title'])}"><a href="index.html">← {t['home_link']}</a>{toc}</nav><article class="legal__body">{body}</article></div></section>
</main>
""",
        footer(lang, pre, t, p, "index.html"),
    ])


def main() -> None:
    (ROOT / "en").mkdir(exist_ok=True)
    for lang in ("es", "en"):
        p = PAGES[lang]
        (ROOT / p["home"]).write_text(home(lang), encoding="utf-8")
        (ROOT / p["privacy"]).write_text(legal(lang, "privacy"), encoding="utf-8")
        (ROOT / p["terms"]).write_text(legal(lang, "terms"), encoding="utf-8")
    print("Web generada.")


if __name__ == "__main__":
    main()
