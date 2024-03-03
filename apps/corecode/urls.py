from django.urls import path

from .views import (
    IndexView,
    SiteConfigView,
    PermitDocCategoryCreateView,
    PermitDocCategoryDeleteView,
    PermitDocCategoryListView,
    PermitDocCategoryUpdateView,
    CitizenshipCreateView,
    CitizenshipDeleteView,
    CitizenshipListView,
    CitizenshipUpdateView,
    DocumentTypeCreateView,
    DocumentTypeDeleteView,
    DocumentTypeListView,
    DocumentTypeUpdateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("site-config", SiteConfigView.as_view(), name="configs"),
    # path(
    #     "current-session/", CurrentSessionAndTermView.as_view(), name="current-session"
    # ),
    # path("session/list/", SessionListView.as_view(), name="sessions"),
    # path("session/create/", SessionCreateView.as_view(), name="session-create"),
    # path(
    #     "session/<int:pk>/update/",
    #     SessionUpdateView.as_view(),
    #     name="session-update",    ),
    # path(
    #     "session/<int:pk>/delete/",
    #     SessionDeleteView.as_view(),
    #     name="session-delete",
    # ),
    # path("term/list/", TermListView.as_view(), name="terms"),
    # path("term/create/", TermCreateView.as_view(), name="term-create"),
    # path("term/<int:pk>/update/", TermUpdateView.as_view(), name="term-update"),
    # path("term/<int:pk>/delete/", TermDeleteView.as_view(), name="term-delete"),
    # path("class/list/", ClassListView.as_view(), name="classes"),
    # path("class/create/", ClassCreateView.as_view(), name="class-create"),
    # path("class/<int:pk>/update/", ClassUpdateView.as_view(), name="class-update"),
    # path("class/<int:pk>/delete/", ClassDeleteView.as_view(), name="class-delete"),
    # path("subject/list/", SubjectListView.as_view(), name="subjects"),
    # path("subject/create/", SubjectCreateView.as_view(), name="subject-create"),
    # path(
    #     "subject/<int:pk>/update/",
    #     SubjectUpdateView.as_view(),
    #     name="subject-update",
    # ),
    # path(
    #     "subject/<int:pk>/delete/",
    #     SubjectDeleteView.as_view(),
    #     name="subject-delete",
    # ),
    path("permitdoccategory/list/", PermitDocCategoryListView.as_view(), name="permitdoccategory"),
    path("permitdoccategory/create/", PermitDocCategoryCreateView.as_view(), name="permitdoccategory-create"),
    path("permitdoccategory/<int:pk>/update/", PermitDocCategoryUpdateView.as_view(), name="permitdoccategory-update"),
    path("permitdoccategory/<int:pk>/delete/", PermitDocCategoryDeleteView.as_view(), name="permitdoccategory-delete"),
    path("citizenship/list/", CitizenshipListView.as_view(), name="citizenship"),
    path("citizenship/create/", CitizenshipCreateView.as_view(), name="citizenship-create"),
    path("citizenship/<int:pk>/update/", CitizenshipUpdateView.as_view(), name="citizenship-update"),
    path("citizenship/<int:pk>/delete/", CitizenshipDeleteView.as_view(), name="citizenship-delete"),
    path("doctype/list/", DocumentTypeListView.as_view(), name="doctype"),
    path("doctype/create/", DocumentTypeCreateView.as_view(), name="doctype-create"),
    path("doctype/<int:pk>/update/", DocumentTypeUpdateView.as_view(), name="doctype-update"),
    path("doctype/<int:pk>/delete/", DocumentTypeDeleteView.as_view(), name="doctype-delete"),
]
