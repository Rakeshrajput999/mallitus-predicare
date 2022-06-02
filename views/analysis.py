import streamlit as st
import codecs
import streamlit.components.v1 as stc

def st_diabatic(diabatic_html,width =700,height =700):
  diabatic_file =codecs.open(diabatic_html,'r')
  page= diabatic_file.read()
  stc.html(page,width=width,height=height,scrolling=True)
    
def load_view():
    st.markdown("""<!DOCTYPE html>
<html lang="en">
  <body>
    <p>
      &nbsp;<span
        style="
          background-color: white;
          font-family: 'Gotham HTF';
          font-size: 15px;
        "
      >
        Diabetes is a condition characterized by elevated blood sugar levels. It
        is currently one of the leading metabolic disorders around the world. As
        per the Lancet report, Type-2 Diabetes is expected to rise by more than
        a fifth, from 406 million in 2018 to 511 million in 2030 globally. About
        98 million Indians are likely to be diagnosed with diabetes by the year
        2030. Type 2 Diabetes could be managed and prevented by eating a healthy
        diet and leading a healthy lifestyle.</span
      >
    </p>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      Understanding how food affects your blood sugar:
    </h5>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      Food has a direct effect on blood glucose. Some foods raise blood glucose
      more than others. An important part of managing diabetes is knowing what
      and how much to eat, and following an eating plan that fits your lifestyle
      while helping to control blood glucose. The 3 main nutrients found in
      foods are carbohydrates (carbs), proteins, and fats.
    </p>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      Carbohydrates (carbs)
    </h5>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      Carbs are the starches, sugar, and fiber in foods such as grains, fruits,
      vegetables, milk products and sweets. They raise blood glucose faster and
      higher than other nutrients in foods: proteins and fats. Knowing what
      foods contain carbs and the amount of carbs in a meal is helpful for blood
      glucose control. Choosing carbs from healthy sources like vegetables,
      fruits and whole grains (high fiber) are preferred over carbs from sources
      with added sugars, fat and salt.
    </p>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      Proteins
    </h5>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      Proteins are a necessary part of a balanced diet and can keep you from
      feeling hungry. They do not directly raise your glucose like carbs.
      However, to prevent weight gain, use portion control with proteins. In
      people with Type 2 diabetes, protein makes insulin work faster, so it may
      not be a good idea to treat low blood sugar with protein shakes or mixes.
    </p>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      Fats
    </h5>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      Fats are a necessary part of a balanced diet, especially healthy fats from
      fatty fish, nuts and seeds. They do not raise blood glucose but are high
      in calories and can cause weight gain.
    </p>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      Aim to include all 3 nutrients to balance your meals.
    </p>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      Planning a Diabetes Diet
    </h5>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      A diabetic diet doesn’t have to be complicated and you don’t have to give
      up all your favorite foods. Here are a few health tips for planning an
      ideal Diabetic diet:
    </p>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      1. Eat more
    </h5>
    <ul
      style="
        background-color: white;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        list-style-type: none;
        margin: 7px 0px 15px;
        padding: 0px;
      "
    >
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Healthy fats from nuts, olive oil, fish oils, flax seeds, or avocados.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Fruits and vegetables—ideally fresh, the more colorful the better; whole
        fruit rather than juices.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Whole grains and millets.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        High-fiber cereals and loaves of bread are made from whole grains.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        High-quality protein such as eggs, beans, low-fat dairy, and unsweetened
        yogurt.
      </li>
    </ul>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      2. Eat less
    </h5>
    <ul
      style="
        background-color: white;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        list-style-type: none;
        margin: 7px 0px 15px;
        padding: 0px;
      "
    >
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Trans fats from partially hydrogenated or deep-fried foods.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Packaged and fast foods, especially those high in sugar, baked goods,
        sweets, chips and desserts.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Foods made from refined flour – bread =, noodles, or portions of pasta.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Processed meat and red meat.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Low-fat products that have replaced fat with added sugar, such as
        fat-free yogurt.
      </li>
    </ul>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      3. Be smart about sweets
    </h5>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      Eating a diabetic diet doesn’t mean eliminating sugar altogether, but like
      most of us, chances are you consume more sugar than is healthy. If you
      have diabetes, you can still enjoy a small serving of your favourite
      dessert now and then. The key is moderation.
    </p>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      Tricks for cutting down on sugar:
    </p>
    <ul
      style="
        background-color: white;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        list-style-type: none;
        margin: 7px 0px 15px;
        padding: 0px;
      "
    >
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Reduce soft drinks, soda and juice.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Don’t replace saturated fat with sugar.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Sweeten foods yourself.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Check labels and look for products with hidden sugar.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Avoid processed or packaged foods.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Reduce the amount of sugar in recipes by ¼ to ⅓.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        Find healthy ways to satisfy your sweet tooth.
      </li>
    </ul>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      3. Be careful with Alcohol
    </h5>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      Do not underestimate the calories and carbs in alcoholic drinks including
      beer and wine. Cocktails mixed with soda and juice can be loaded with
      sugar. Liquid calories can also spike up your blood sugar levels.
    </p>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      4. Choose fats wisely
    </h5>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      Some fats are unhealthy and others have enormous health benefits, so it’s
      important to choose fats wisely.
    </p>
    <ul
      style="
        background-color: white;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        list-style-type: none;
        margin: 7px 0px 15px;
        padding: 0px;
      "
    >
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        <span
          style="
            border: 0px;
            box-sizing: border-box;
            font-weight: 700;
            margin: 0px;
            outline: 0px;
            padding: 0px;
          "
          >Unhealthy fats.</span
        >&nbsp;The most damaging fats are artificial trans fats, which make
        vegetable oils less likely to spoil. Avoid commercially-baked goods,
        packaged snack foods, fried food, and anything with “partially
        hydrogenated” oil in the ingredients, even if it claims to be trans
        fat-free.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        <span
          style="
            border: 0px;
            box-sizing: border-box;
            font-weight: 700;
            margin: 0px;
            outline: 0px;
            padding: 0px;
          "
          >Healthy fats.</span
        >&nbsp;The healthiest fats are unsaturated fats, which come from fish
        and plant sources such as olive oil, nuts, and avocados. Omega-3 fatty
        acids fight inflammation and support brain and heart health. Good
        sources include salmon, tuna, and flaxseeds.
      </li>
      <li
        style="
          box-sizing: border-box;
          line-height: 24px;
          list-style-type: none;
          margin: 0px 0px 5px 15px;
          padding: 0px 0px 5px;
          position: relative;
        "
      >
        <span
          style="
            border: 0px;
            box-sizing: border-box;
            font-weight: 700;
            margin: 0px;
            outline: 0px;
            padding: 0px;
          "
          >Saturated fats.</span
        >&nbsp;Found mainly in tropical oils, red meat, and dairy, there’s no
        need to completely eliminate saturated fat from your diet—but rather,
        enjoy it in moderation.
      </li>
    </ul>
    <h5
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        color: #ff4b64;
        font-family: 'Gotham HTF';
        font-size: 18px;
        line-height: normal;
        margin: 0px;
        outline: 0px;
        padding: 10px 0px;
      "
    >
      5. Eat regularly and keep a food diary
    </h5>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      It’s encouraging to know that you only have to lose 7% of your body weight
      to cut your risk of diabetes in half. And you don’t have to obsessively
      count calories or starve yourself to do it. Two of the most helpful
      strategies involve following a regular eating schedule and recording what
      you eat.
    </p>
    <p
      style="
        background-color: white;
        border: 0px;
        box-sizing: border-box;
        font-family: 'Gotham HTF';
        font-size: 15px;
        line-height: 25px;
        margin: 0px 0px 10px;
        outline: 0px;
        padding: 0px;
      "
    >
      Are you suffering from Diabetes? Consult our team of Nutritionists who can
      guide you with personalized diet plans to control your Diabetes and lead a
      normal life.
    </p>

    >>>>>>> 2f4138cb136cd0e6fe16fe424f63c6e45d9052cc
  </body>
</html>
""",unsafe_allow_html=True)