from collections import OrderedDict
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from users.models import User
import pandas
import datetime
import json


# Create your views here.
class PostPagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'page'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('items_total', self.page.paginator.count),
            ('items_in_page', self.page_size),
            ('current_page', self.page.number),
            ('total_pages', self.page.paginator.num_pages),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PostPagination

    if Post.objects.all().count() == 0:
        author = User.objects.all().first()
        is_public = True

        data = [
            {
                "title": "In Loving Memory of John Smith",
                "birth_date": "1950-01-01",
                "death_date": "2023-02-15",
                "content": "<p>John Smith was a beloved husband, father, grandfather, brother and friend. He passed away peacefully at his home surrounded by his family. He was 73 years old.</p><p>John was born in New York City to Robert and Helen Smith. He grew up in Brooklyn with his three siblings: James, Susan and Lisa. He attended Brooklyn College and graduated with a degree in accounting. He worked as a CPA for over 40 years at various firms.</p><p>John married his high school sweetheart, Mary Jones, in 1972. They had two children: Peter and Laura. John loved spending time with his family, especially his four grandchildren: Anna, Ryan, Emma and Noah. He enjoyed playing golf, reading books and watching movies.</p><p>John was a kind, generous and loyal person who always had a smile on his face. He touched many lives with his humor and wisdom. He will be deeply missed by all who knew him.</p><p>A memorial service will be held on Saturday, March 4th at 11:00 am at St. Patrick's Church in Brooklyn. In lieu of flowers, donations can be made to the American Cancer Society in John's name.</p>"
            },
            {
                "title": "Remembering Jane Doe",
                "birth_date": "1965-05-10",
                "death_date": "2023-03-01",
                "content": "<p>Jane Doe was a loving wife, mother, daughter, sister and friend. She passed away unexpectedly at the hospital after a short illness. She was 57 years old.</p><p>Jane was born in Chicago to Frank and Alice Johnson. She grew up in Evanston with her two brothers: Mark and Paul. She attended Northwestern University and graduated with a degree in journalism. She worked as a reporter for the Chicago Tribune for over 30 years.</p><p>Jane married her college sweetheart, David Doe, in 1988. They had three children: Michael, Sarah and Emily. Jane loved traveling with her family, writing stories and volunteering at her local animal shelter.</p><p>Jane was a compassionate, creative and courageous person who always stood up for what she believed in. She inspired many people with her passion and integrity. She will be dearly missed by all who knew her.</p><p>A memorial service will be held on Sunday, March 12th at 2:00 pm at the Evanston Public Library Auditorium. In lieu of flowers, donations can be made to the ASPCA in Jane's name.</p>"
            },
            {
                "title": "A Tribute to Alice Lee",
                "birth_date": "1975-08-15",
                "death_date": "2023-01-20",
                "content": "<p>Alice Lee was a wonderful wife, mother, sister and friend. She passed away peacefully at the hospice after a long battle with ALS. She was 47 years old.</p><p>Alice was born in San Francisco to George and Linda Wong. She grew up in Oakland with her sister: Kelly. She attended UC Berkeley and graduated with a degree in computer science. She worked as a software engineer for Google for over 20 years.</p><p>Alice married her best friend, Kevin Lee, in 1999. They had two children: Jason and Lily. Alice loved hiking with her family, coding games and baking cookies.</p><p>Alice was a smart, cheerful and generous person who always helped others. She faced her illness with grace and courage. She will be forever remembered by all who knew her.</p><p>A memorial service will be held on Saturday, February 11th at 10:00 am at the Oakland Chinese Church. In lieu of flowers, donations can be made to the ALS Association in Alice's name.</p>"
            },
            {
                "title": "Celebrating the Life of Robert Jones",
                "birth_date": "1940-03-05",
                "death_date": "2023-02-28",
                "content": "<p>Robert Jones was a devoted husband, father, grandfather, uncle and friend. He passed away peacefully at his home surrounded by his family. He was 82 years old.</p><p>Robert was born in Boston to Edward and Mary Jones. He grew up in Quincy with his four siblings: Charles, Elizabeth, William and Margaret. He attended Harvard University and graduated with a degree in law. He worked as a lawyer for over 50 years at various firms.</p><p>Robert married his childhood sweetheart, Helen Smith, in 1962. They had four children: Richard, Jennifer, Thomas and Catherine. Robert loved spending time with his family, especially his eight grandchildren: Jessica, Matthew, Daniel, Sophia, Olivia, James, Ethan and Abigail. He enjoyed playing chess, gardening and watching sports.</p><p>Robert was a wise, honest and faithful person who always gave good advice. He mentored many young lawyers with his experience and knowledge. He will be greatly missed by all who knew him.</p><p>A memorial service will be held on Friday, March 10th at 1:00 pm at the Quincy First Baptist Church. In lieu of flowers, donations can be made to the Alzheimer's Association in Robert's name.</p>"
            },
            {
                "title": "Honoring the Memory of Mary Wilson",
                "birth_date": "1955-06-20",
                "death_date": "2023-01-25",
                "content": "<p>Mary Wilson was a caring wife, mother, grandmother, aunt and friend. She passed away peacefully at the hospital after a heart attack. She was 67 years old.</p><p>Mary was born in Los Angeles to Jack and Rose Miller. She grew up in Pasadena with her two sisters: Nancy and Karen. She attended UCLA and graduated with a degree in nursing. She worked as a nurse for over 40 years at various hospitals.</p><p>Mary married her soulmate, John Wilson, in 1978. They had three children: Brian, Amy and Scott. Mary loved cooking for her family, knitting sweaters and playing piano.</p><p>Mary was a gentle, kind and nurturing person who always cared for others. She was a devoted member of her church and a volunteer at her local food bank. She will be fondly remembered by all who knew her.</p><p>A memorial service will be held on Wednesday, February 8th at 3:00 pm at the Pasadena Community Church. In lieu of flowers, donations can be made to the American Heart Association in Mary's name.</p>"
            },
            {
                "title": "A Celebration of Life for James Brown",
                "birth_date": "1960-09-15",
                "death_date": "2023-02-20",
                "content": "<p>James Brown was a fun-loving husband, father, brother and friend. He passed away unexpectedly at his office after an aneurysm. He was 62 years old.</p><p>James was born in Houston to Samuel and Dorothy Brown. He grew up in Sugar Land with his three brothers: David, Michael and Steven. He attended Texas A&M University and graduated with a degree in engineering. He worked as an engineer for ExxonMobil for over 30 years.</p><p>James married his college sweetheart, Lisa Green, in 1985. They had two children: Chris and Megan. James loved fishing with his family, playing guitar and making jokes.</p><p>James was a smart, funny and adventurous person who always lived life to the fullest. He was a loyal friend and a mentor to many young engineers. He will be dearly missed by all who knew him.</p><p>A memorial service will be held on Saturday, March 18th at 11:00 am at the Sugar Land Memorial Park. In lieu of flowers, donations can be made to the Brain Aneurysm Foundation in James' name.</p>"
            },
            {
                "title": "In Loving Memory of John Smith",
                "birth_date": "1950-01-01",
                "death_date": "2023-02-28",
                "content": "<p>John Smith was a loving husband, father, grandfather and friend. He passed away peacefully on February 28th, 2023 at the age of 73. He was born on January 1st, 1950 in New York City, where he lived most of his life. He worked as a journalist for The New York Times for over 40 years, covering many important stories and events. He was passionate about writing, reading, traveling and music.</p><p>He is survived by his wife of 50 years, Jane Smith; his children, David Smith (Lisa), Laura Jones (Mark) and Sarah Wilson (Tom); his grandchildren, Emily, Ryan, Anna and Noah; his sister, Mary Brown (Bob); and many nieces, nephews and friends.</p><p>A memorial service will be held on Saturday, March 4th at 11:00 am at St. John's Church in Manhattan. In lieu of flowers, donations can be made to the Alzheimer's Association in John's name.</p><p>We will miss him dearly and remember him always.</p>"
            },
            {
                "title": "A Tribute to Alice Lee",
                "birth_date": "1975-06-15",
                "death_date": "2023-03-10",
                "content": "<p>Alice Lee was a remarkable woman who touched many lives with her kindness, generosity and courage. She died on March 10th, 2023 after a long battle with cancer. She was 47 years old.</p><p>Alice was born on June 15th, 1975 in San Francisco, California. She graduated from Stanford University with a degree in computer science and worked as a software engineer at Google for over 20 years. She was a pioneer in her field and a mentor to many young professionals.</p><p>Alice loved nature, animals and adventure. She traveled to over 30 countries and volunteered for various environmental and humanitarian causes. She also enjoyed hiking, biking, skiing and surfing.</p><p>Alice is survived by her husband of 25 years, James Lee; her daughter Lily Lee; her parents Robert and Helen Chen; her brother Kevin Chen (Julia); her sister Jennifer Wong (Eric); her nieces and nephews; and countless friends who loved her like family.</p><p>A celebration of life will be held on Sunday March 19th at 2:00 pm at Golden Gate Park in San Francisco. Please wear colorful clothes to honor Alice's vibrant spirit. In lieu of flowers please consider making a donation to the World Wildlife Fund or Doctors Without Borders in Alice's memory.</p><p>Alice was an inspiration to us all and we will never forget her smile.</p>"
            },
            {
                "title": "Remembering Robert Jones",
                "birth_date": "1960-03-21",
                "death_date": "2023-03-15",
                "content": "<p>Robert Jones was a devoted husband, father, brother and friend. He passed away unexpectedly on March 15th, 2023 at the age of 63. He was born on March 21st, 1960 in Chicago, Illinois. He graduated from Northwestern University with a degree in law and worked as a successful attorney for over 30 years. He was respected by his colleagues and clients for his integrity, professionalism and compassion.</p><p>Robert loved his family more than anything. He married his high school sweetheart, Susan Jones, in 1982 and they had three children: Michael, Jessica and Daniel. He was a proud and supportive father who always encouraged his children to follow their dreams. He also adored his four grandchildren: Olivia, Ethan, Emma and Noah.</p><p>Robert enjoyed playing golf, watching sports, reading books and spending time with his friends. He had a great sense of humor and a warm personality that made everyone feel welcome.</p><p>A funeral service will be held on Friday March 24th at 10:00 am at Grace Church in Chicago. Burial will follow at Oak Hill Cemetery. In lieu of flowers please make a donation to the American Heart Association or the Salvation Army in Robert's name.</p><p>We will always remember Robert's smile and his love for life.</p>"
            },
            {
                "title": "Celebrating the Life of Lisa Martin",
                "birth_date": "1985-09-10",
                "death_date": "2023-03-12",
                "content": "<p>Lisa Martin was a beautiful soul who left us too soon on March 12th, 2023 at the age of 37. She was born on September 10th, 1985 in Los Angeles, California. She studied art at UCLA and became a talented painter and photographer. She exhibited her work in several galleries and won several awards for her creativity.</p><p>Lisa had a passion for helping others. She volunteered for various charities and causes such as Habitat for Humanity, Make-A-Wish Foundation and Animal Rescue League. She also taught art classes to underprivileged children and seniors.</p><p>Lisa was a loving daughter, sister, aunt and friend. She is survived by her parents John and Karen Martin; her brother Matt Martin (Kelly); her sister Amy Johnson (Brian); her nieces Chloe and Zoe; her nephew Tyler; her best friend Sarah Green; and many other relatives and friends who loved her dearly.</p><p>A memorial service will be held on Saturday March 18th at 1:00 pm at The Art Center in Los Angeles. Please join us to celebrate Lisa's life and legacy through her art work which will be displayed at the venue. In lieu of flowers please consider making a donation to one of Lisa's favorite charities or organizations.</p><p>Lisa was an angel on earth who touched many hearts with her kindness, generosity and beauty.</p>"
            },
            {
                "title": "Paying Tribute to Anna Lee",
                "birth_date": "1970-01-15",
                "death_date": "2023-03-17",
                "content": "<p>Anna Lee was a remarkable woman who inspired many people with her courage and grace. She passed away on March 17th, 2023 at the age of 53 after a long battle with cancer. She was born on January 15th, 1970 in New York City. She graduated from Columbia University with a degree in journalism and became a reporter for The New York Times. She covered many important stories and won several awards for her excellence and professionalism.</p><p>Anna was a devoted wife, mother, sister and friend. She married her college sweetheart, James Lee, in 1992 and they had two sons: Alex and Ryan. She was a loving and supportive mother who always encouraged her sons to pursue their passions. She also had a close bond with her sister Kate Brown (Tom) and her brother John Smith (Lisa). She cherished her friendships with many people who admired her for her honesty, generosity and humor.</p><p>A memorial service will be held on Wednesday March 22nd at 2:00 pm at The New York Times Building in New York City. Please join us to honor Anna's life and legacy through her words and pictures which will be displayed at the venue. In lieu of flowers please consider making a donation to The American Cancer Society or The New York Times Neediest Cases Fund in Anna's name.</p><p>Anna was a shining star who touched many lives with her wisdom, compassion and beauty.</p>"
            },
            {
                "title": "Celebrating Mary Jones",
                "birth_date": "1940-12-25",
                "death_date": "2023-03-20",
                "content": "<p>Mary Jones was a loving and joyful woman who spread happiness wherever she went. She passed away on March 20th ,2023 at the age of 82 due to natural causes. She was born on December 25th ,1940 in Chicago, Illinois. She studied art at The Art Institute of Chicagoand became an acclaimed painter. She exhibited her works in many galleriesand museumsand won several awards for her creativityand originality. </p><p>Mary was married to Robert Jones for sixty years until he preceded her in death five years ago. They had two daughters : Laura Smith (Mark)and Linda Johnson (Eric). They also had four grandchildren : Amy, Brian, Kellyand Jason. Mary was a warmand nurturing motherand grandmother who always showered her family with loveand affection. She also had a strong bond with her sister Jane Miller (Tom); her brother Jack Smith (Nancy); her nieces Nicoleand Emma; her nephews Peterand Ryan ;and her friends from the art community. She loved spending time with her family especially during birthdays. She also enjoyed baking, knitting, gardening ,and playing piano </p><p>A memorial service will be held on Friday March24th at2:00 pmat The Art Museumin Chicago. Please join us to celebrate Mary's lifeand legacy through her paintings which will be displayedat the venue.In lieu offlowers please make adonationto The Art Institute of Chicagoor The Alzheimer's Associationin Mary'name </p><p>Mary was an artistwho created beautyin the world.We will always remember her smile</p>"
            },
            {
                "title": "A Tribute to John Smith",
                "birth_date": "1930-05-01",
                "death_date": "2023-03-21",
                "content": "<p>John Smith was a wise and generous man who made a difference in many lives. He passed away on March 21st, 2023 at the age of 92 due to pneumonia. He was born on May 1st, 1930 in London, England. He studied law at Oxford University and became a renowned lawyer and judge. He defended many cases of human rights and justice and earned respect and admiration from his peers and clients.</p><p>John was married to Elizabeth Smith for seventy years and they had four sons: James, David, Richard and Edward. He was a loving and supportive husband and father who always gave his family the best advice and guidance. He also had a close relationship with his sister Margaret Brown (George); his brother William Smith (Anne); his nieces Lucy and Alice; his nephews Henry and Charles; and his friends from the legal profession. He loved spending time with his family especially during Christmas. He also liked reading, writing, chess and golf.</p><p>A memorial service will be held on Monday March 27th at 11:00 am at The Westminster Abbey in London. Please join us to honor John's life and legacy through his words and deeds which will be remembered by his colleagues and family members who will speak at the service. In lieu of flowers please consider making a donation to The Human Rights Watch or The British Red Cross in John's name.</p><p>John was a leader who stood for truth and fairness.</p>"
            },
            {
                "title": "In Loving Memory of Lisa Davis",
                "birth_date": "1985-09-15",
                "death_date": "2023-03-22",
                "content": "<p>Lisa Davis was a beautiful and kind woman who touched many hearts with her smile. She passed away on March 22nd ,2023 at the age of 37 due to breast cancer. She was born on September 15th ,1985 in Los Angeles, California. She studied fashion design at The Fashion Institute of Design & Merchandisingand became a successful designer. She created many stunning collectionsand worked with famous brandsand celebrities. She was an icon of styleand elegance. </P<p>Lisa was married to Ryan Davis for ten yearsand they had one daughter : Mia Davis. She was a lovingand fun-loving wifeand mother who always made her family happy. She also had a strong bond with her parents Markand Karen Johnson; her sister Kelly Wilson (Brad); her brother Mike Johnson (Sara); her nieces Emmaand Zoe; her nephew Ethan ;and her friends from the fashion industry. She loved spending time with her family especially during Halloween. She also enjoyed shopping, dancing, yoga ,and watching movies </P<p>A celebration of life service will be held on Thursday March30th at4:00 pmat The Beverly Hills Hotelin Los Angeles. Please join us to celebrate Lisa's lifeand legacy through her photos which will be displayedat the venue.Please wear something pinkto honor Lisa's favorite color.In lieu offlowers please make adonationto The Susan G.Komen Foundationor The Make-A-Wish Foundationin Lisa'name </P<p>Lisa was an angelwho brought joyto the world.We will always remember her beauty</p>"
            },
            {
                "title": "In Loving Memory of John Smith",
                "content": "<p>John Smith, a beloved husband and father, passed away on February 1, 2022. He was born on January 1, 1950, and is survived by his wife and two children. John will be dearly missed by all who knew him.</p>",
                "birth_date": "1950-01-01",
                "death_date": "2022-02-01"
            },
            {
                "title": "Remembering Anna Garcia",
                "content": "<p>Anna Garcia, a dear friend and colleague, passed away on January 17, 2022. She was born on May 12, 1985, and is survived by her parents and siblings. Anna will always be remembered for her kindness and generosity.</p>",
                "birth_date": "1985-05-12",
                "death_date": "2022-01-17"
            },
            {
                "title": "Tribute to Emily Chen",
                "content": "<p>Emily Chen, a loving mother and wife, passed away on February 14, 2023. She was born on November 3, 1972, and is survived by her husband and two children. Emily will be greatly missed by her family and friends.</p>",
                "birth_date": "1972-11-03",
                "death_date": "2023-02-14"
            },
            {
                "title": "Remembering Anna Lee",
                "birth_date": "1975-06-20",
                "death_date": "2023-03-23",
                "content": "<p>Anna Lee was a bright and adventurous woman who lived life to the fullest. She passed away on March 23rd, 2023 at the age of 47 due to a car accident. She was born on June 20th, 1975 in New York City, New York. She studied journalism at Columbia University and became a travel writer and photographer. She traveled around the world and shared her stories and pictures with millions of readers and followers.</p><p>Anna was married to Tom Lee for twenty years and they had two dogs: Max and Luna. She was a loving and loyal wife who always supported her husband's dreams and goals. She also had a close relationship with her parents John and Mary Wilson; her sister Emily Green (Jack); her brother Chris Wilson (Kate); her nieces Sophie and Lily; her nephews Noah and Liam; and her friends from the journalism industry. She loved spending time with her family especially during Thanksgiving. She also enjoyed hiking, skiing, scuba diving, and cooking.</p><p>A celebration of life service will be held on Saturday April 1st at 3:00 pm at The Central Park in New York City. Please join us to remember Anna's life and legacy through her words and images which will be displayed at the venue. Please bring your favorite memories or stories of Anna to share with others. In lieu of flowers please consider making a donation to The World Wildlife Fund or The National Geographic Society in Anna's name.</p><p>Anna was an explorer who inspired us to see the world.</p>"
            },
            {
                "title": "Celebrating the Life of David Jones",
                "birth_date": "1960-04-10",
                "death_date": "2023-03-25",
                "content": "<p>David Jones was a talented and passionate man who left a mark on the world with his music. He passed away on March 25th, 2023 at the age of 62 due to a heart attack. He was born on April 10th, 1960 in Liverpool, England. He studied music at The Royal Academy of Music and became a rock star. He formed the band The Beatles with his friends John Lennon, Paul McCartney and George Harrison. He wrote and sang many hit songs that influenced generations of fans and musicians.</p><p>David was married to Linda Jones for thirty years and they had two sons: Paul and George. He was a loving and supportive husband and father who always encouraged his family to pursue their dreams. He also had a close relationship with his parents Harry and Mary Jones; his sister Jane Smith (Peter); his brother Mike Jones (Julia); his nieces Anna and Lucy; his nephews John and James; and his friends from the music industry. He loved spending time with his family especially during New Year's Eve. He also enjoyed playing guitar, painting, traveling, and meditating.</p><p>A tribute concert will be held on Sunday April 2nd at 7:00 pm at The Wembley Stadium in London. Please join us to celebrate David's life and legacy through his songs which will be performed by his bandmates, family members, colleagues and admirers who will also speak at the concert. Please wear something colorful to honor David's vibrant personality. In lieu of flowers please consider making a donation to The Save The Children or The MusiCares Foundation in David's name.</p><p>David was an artist who moved us with his voice.</p>"
            },
            {
                "title": "In Loving Memory of John Smith",
                "content": "<p>John Smith, a beloved husband and father, passed away on February 1, 2022. He will be deeply missed by his family and friends.</p>",
                "birth_date": "1950-01-01",
                "death_date": "2022-02-01"
            },
            {
                "title": "Remembering Anna Garcia",
                "content": "<p>Anna Garcia, a dear friend and colleague, passed away on January 17, 2022. She will be remembered for her kindness and generosity.</p>",
                "birth_date": "1985-05-12",
                "death_date": "2022-01-17"
            },
            {
                "title": "Tribute to Emily Chen",
                "content": "<p>Emily Chen, a loving mother and wife, passed away on February 14, 2023. She will always be remembered for her warmth and grace.</p>",
                "birth_date": "1972-11-03",
                "death_date": "2023-02-14"
            },
            {
                "title": "Celebrating the Life of William Lee",
                "content": "<p>William Lee, a dedicated community leader, passed away on March 9, 2022. He will be remembered for his tireless work to make our community a better place.</p>",
                "birth_date": "1960-06-23",
                "death_date": "2022-03-09"
            },
            {
                "title": "Honoring the Memory of David Kim",
                "content": "<p>David Kim, a talented musician and beloved friend, passed away on April 18, 2022. He will be deeply missed by all who knew him.</p>",
                "birth_date": "1987-09-01",
                "death_date": "2022-04-18"
            },
            {
                "title": "In Remembrance of Maria Rodriguez",
                "content": "<p>Maria Rodriguez, a kind-hearted mother and grandmother, passed away on May 22, 2022. She will always be remembered for her love and warmth.</p>",
                "birth_date": "1978-03-14",
                "death_date": "2022-05-22"
            },
            {
                "title": "Remembering Mark Thompson",
                "content": "<p>Mark Thompson, a devoted husband and father, passed away on March 27, 2022. He will be deeply missed by his family and friends.</p>",
                "birth_date": "1965-08-17",
                "death_date": "2022-03-27"
            },
            {
                "title": "A Celebration of the Life of Rachel Davis",
                "content": "<p>Rachel Davis, a compassionate nurse and beloved wife, passed away on May 10, 2022. She will always be remembered for her kindness and dedication to her patients.</p>",
                "birth_date": "1982-01-07",
                "death_date": "2022-05-10"
            },
            {
                "title": "Honoring the Memory of Daniel Perez",
                "content": "<p>Daniel Perez, a dedicated teacher and beloved father, passed away on June 5, 2022. He will be deeply missed by his students and family.</p>",
                "birth_date": "1970-11-28",
                "death_date": "2022-06-05"
            },
            {
                "title": "In Memory of Sarah Johnson",
                "content": "<p>Sarah Johnson, a beloved mother, sister, and friend, passed away on August 1, 2021. She will be deeply missed by all who knew her.</p><p>Sarah was born on December 12, 1965, in Chicago, Illinois. She grew up in a large family and was always the life of the party. She loved to dance and sing, and her infectious laughter could light up a room. She had a passion for cooking and often hosted elaborate dinner parties for her friends and family.</p><p>Sarah was a dedicated nurse and worked for over 25 years in the emergency room. She was known for her kindness and compassion, and her patients often remarked on her calming presence. She was also an active member of her church and volunteered her time to various community organizations.</p><p>Sarah will be remembered for her infectious spirit, her kind heart, and her unwavering devotion to her family and friends. She leaves behind her daughter, siblings, nieces and nephews, and a legacy of love and generosity that will live on for generations to come.</p>",
                "birth_date": "1965-12-12",
                "death_date": "2021-08-01"
            },
            {
                "title": "Honoring the Life of James Brown",
                "content": "<p>James Brown, a respected community leader and philanthropist, passed away on June 15, 2022. He leaves behind a legacy of service and compassion.</p><p>James was born on January 2, 1950, in Atlanta, Georgia. He grew up in a segregated neighborhood and witnessed firsthand the injustices of racism. He became an activist in his teenage years and spent his life fighting for equality and justice. He was a founding member of the local chapter of the NAACP and served as its president for over 20 years.</p><p>James was also a successful businessman and owned several restaurants and real estate properties. He was known for his generosity and often donated to local charities and organizations. He was a devoted husband and father and always put his family first.</p><p>James will be deeply missed by his family, friends, and community. His unwavering commitment to justice and equality will continue to inspire future generations to make a difference in the world.</p>",
                "birth_date": "1950-01-02",
                "death_date": "2022-06-15"
            }
        ]

        for row in data:
            print(row)
            title = row["title"]
            content = row["content"]
            birth_date = datetime.datetime.strptime(row["birth_date"], "%Y-%m-%d")
            death_date = datetime.datetime.strptime(row["death_date"], "%Y-%m-%d")

            Post(
                author=author,
                title=title,
                content=content,
                birth_date=birth_date,
                death_date=death_date,
            ).save()

