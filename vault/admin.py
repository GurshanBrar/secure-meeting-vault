from django.contrib import admin
from .models import Group, Member


class MembersInline(admin.TabularInline):
    model = Member

    exclude = ['encoded_file']
    extra = 0


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'meeting_url')
    inlines = [MembersInline]


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group',)

    exclude = ['encoded_file']


admin.site.register(Member, MemberAdmin)
