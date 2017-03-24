# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class JitopMacro(BrowserView):

    def __call__(self):
        folderName = ['about', 'service', 'showcase', 'partner', 'media']
        self.results = {}

        for folderItem in folderName:
            self.results[folderItem] = []
            brain = portal[folderItem].getChildNodes()
            for item in brain:
                if item.Type() == 'Page':
                    self.results[folderItem].append(item)
