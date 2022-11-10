from trivy import trivy
import clam.clamservice
application = clam.clamservice.run_wsgi(trivy)