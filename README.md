# GitHub Codespaces ♥️ Django

Welcome to your shiny new Codespace running Django! We've got everything fired up and running for you to explore Django.

You've got a blank canvas to work on from a git perspective as well. There's a single initial commit with what you're seeing right now - where you go from here is up to you!

Everything you do here is contained within this one codespace. There is no repository on GitHub yet. If and when you’re ready you can click "Publish Branch" and we’ll create your repository and push up your project. If you were just exploring then and have no further need for this code then you can simply delete your codespace and it's gone forever.

## installing dependancies

```python
pip install -r requirements.txt
```

## To collect static files:

```python
python manage.py collectstatic
```

## To run this application:

```python
python manage.py runserver
```

## Ücretsiz canlıya alma (Render)

1. VS Code'da **Publish Branch** ile projeyi GitHub'a gönder.
2. Render hesabında **New + → Blueprint** seçip GitHub deposunu bağla.
3. Depodaki `render.yaml` ayarlarını onaylayıp deploy et.
4. Deploy tamamlandığında Render'ın verdiği `.onrender.com` adresini aç.

Ücretsiz web servisi bir süre trafik almazsa uykuya geçebilir; ilk açılış yavaş olabilir. Ücretsiz diskteki SQLite verileri kalıcı değildir. Bu RCU aracı veriyi tarayıcıda işlediğinden kullanıcı girdileri sunucuda saklanmaz.
