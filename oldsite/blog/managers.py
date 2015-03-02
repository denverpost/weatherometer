# Managers
class PublishedManager(models.Manager):
    def get_query_set(self):
        return super(PublishedManager,
                  self).get_query_set().filter(is_live=True)