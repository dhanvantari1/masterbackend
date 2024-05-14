from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    MinValueValidator,
)
from decimal import Decimal


class TenantMaster(models.Model):
    """
    Model representing Tenant_Master.
    """

    # Primary key for the tenant
    tenant_id = models.AutoField(primary_key=True)
    
    # Code of the tenant
    tenant_code = models.CharField(max_length=10, null=False)

    # Name of the tenant
    tenant_name = models.CharField(max_length=255, unique=True, null=False)

    # URL of the tenant
    tenant_url = models.CharField(max_length=255, null=False)

    # Database connection string of the tenant
    tenant_db_string = models.CharField(max_length=255, null=False)

    # Database server of the tenant
    tenant_db_server = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.tenant_name

    class Meta:
        db_table = "tenant_master"

class CommodityGroup(models.Model):
    """
    Model representing CMD Group.
    """

    cmd_group_id = models.AutoField(primary_key=True)

    # Foreign key to the TenantMaster table
    fk_tenant_id = models.ForeignKey(TenantMaster, on_delete=models.CASCADE, null=False)

    # Tenant code
    tenant_code = models.CharField(max_length=10, null=False)

    # Name of the CMD Discipline
    cmd_discpln_name = models.CharField(max_length=255)

    # Name of the CMD Group
    cmd_group_name = models.CharField(max_length=255)

    def __str__(self):
        return self.cmd_group_name

    class Meta:
        db_table = "commodity_group"

class Commodity(models.Model):
    """
    Model representing Commodity.
    """

    # Primary key for the commodity
    cmd_id = models.AutoField(primary_key=True)

    fk_tenant_id = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)

    tenant_code = models.CharField(max_length=10, null=False)

    fk_cmd_group_id = models.ForeignKey(CommodityGroup, on_delete=models.CASCADE)

    # Name of the commodity
    cmd_name = models.CharField(max_length=255, unique=True, null=False)

    # Description of the commodity
    cmd_desc = models.TextField()

    # Unit of measurement for the commodity
    cmd_unit = models.CharField(max_length=50, null=False)

    # Weight of the commodity
    cmd_weight = models.DecimalField(
        max_digits=10, decimal_places=2
    )

    # Time when the commodity was created
    cmd_created_time = models.DateTimeField(auto_now_add=True)

    # Time when the commodity was last updated
    cmd_updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    # Created By
    cmd_created_by = models.CharField(max_length=255, null=True, blank=True)

    # Updated By
    cmd_updated_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.cmd_name

    class Meta:
        db_table = "commodity"


class Country(models.Model):
    """
    Model representing Country.
    """

    # Primary key for the country
    country_id = models.AutoField(primary_key=True)

    # Name of the country
    country_name = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return self.country_name

    class Meta:
        db_table = "country"


class State(models.Model):
    """
    Model representing State.
    """

    # Primary key for the state
    state_id = models.AutoField(primary_key=True)

    # Name of the state
    state_name = models.CharField(max_length=255, unique=True, null=False)

    state_code = models.CharField(max_length=10, unique=True, null=False)

    # Foreign key to the Country table
    state_country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_name

    class Meta:
        db_table = "state"


"""
    Model representing Groups.
"""


class Group(models.Model):
    # Primary key for the group
    group_id = models.AutoField(primary_key=True)

    # Name of the group
    group_name = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = "group"





class Parameter(models.Model):

    """
    Model representing Parameters.
    """

    # Primary key for the parameter
    param_id = models.AutoField(primary_key=True)

    fk_tenant_id = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)

    tenant_code = models.CharField(max_length=10, null=False)

    # Name of the parameter
    param_name = models.CharField(max_length=255, unique=True, null=False)

    # Description of the parameter
    param_desc = models.TextField()

    param_unit = models.CharField(max_length=50, null=False)

    param_unitsymbol = models.CharField(max_length=10, null=False)

    # Time when the parameter was created
    param_created_time = models.DateTimeField(auto_now_add=True)

    # Time when the parameter was last updated
    param_updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    # Created By
    param_created_by = models.CharField(max_length=255, null=True, blank=True)

    # Updated By
    param_updated_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.param_name

    class Meta:
        db_table = "parameter"


class Standard(models.Model):
    """
    Model representing Standard.
    """

    # Primary key for the standard
    std_id = models.AutoField(primary_key=True)

    fk_tenant_id = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)

    tenant_code = models.CharField(max_length=10, null=False)

    # Name of the standard
    std_name = models.CharField(max_length=255, unique=True, null=False)

    # Description of the standard
    std_desc = models.TextField()

    # Time when the standard was created
    std_created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # Time when the standard was last updated
    std_updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    # Created By
    std_created_by = models.CharField(max_length=255, null=True, blank=True)

    # Updated By
    std_updated_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.std_name

    class Meta:
        db_table = "standard"


class Company(models.Model):
    """
    Model representing Company.
    """

    # Primary key for the company
    cmp_id = models.AutoField(primary_key=True)

    fk_tenant_id = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)

    tenant_code = models.CharField(max_length=10, null=False)

    # Name of the company
    cmp_name = models.CharField(max_length=255, null=False)
    

    # Address of the company
    cmp_address = models.TextField()

    cmp_code = models.CharField(max_length=10, null=False)

    # Email of the company
    cmp_email = models.EmailField(unique=True)

    # State of the company
    cmp_state = models.ForeignKey(State, on_delete=models.CASCADE, null=False)

    # Country of the company
    cmp_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)

    # Phone number of the company
    cmp_phoneno = models.CharField(
        max_length=10,
        unique=True,
        validators=[MinLengthValidator(10), MaxLengthValidator(10)],
    )

    # PAN number of the company
    cmp_pan_no = models.CharField(max_length=255,  null=False)

    # CIN number of the company
    cmp_cin_no = models.CharField(max_length=255, null=False)

    # GST number of the company
    cmp_gst_no = models.CharField(max_length=255, null=False)

    # IEC number of the company
    cmp_iec_no = models.CharField(max_length=255,  null=False)

    cmp_seal = models.CharField(max_length=255, null=False)

    cmp_stamp = models.TextField()

    cmp_compliance_authority = models.TextField()
    
    # Time when the company was created
    cmp_created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # Time when the company was last updated
    cmp_updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    # Created By
    cmp_created_by = models.CharField(max_length=255, null=True, blank=True)

    # Updated By
    cmp_updated_by = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.cmp_name

    class Meta:
        db_table = "company"


class Branch(models.Model):
    """
    Model representing Branch.
    """

    # Primary key for the branch
    br_id = models.AutoField(primary_key=True)

    fk_tenant_id = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)

    tenant_code = models.CharField(max_length=10, null=False)

    # Name of the branch
    br_name = models.CharField(max_length=255, unique=True, null=False)

    # Phone number of the branch
    br_phoneno = models.CharField(
        max_length=10,
        unique=True,
        validators=[MinLengthValidator(10), MaxLengthValidator(10)],
    )

    br_code = models.CharField(max_length=10, unique=True, null=False)

    # Email of the branch
    br_email = models.EmailField(unique=True, null=False)

    # Address of the branch
    br_address = models.TextField()

    # Location of the branch
    br_location = models.CharField(max_length=255)

    # Postal code of the branch
    br_postal_code = models.CharField(max_length=255, null=False)

    # Foreign key to the Company table
    fk_compid = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)

    cmp_code = models.CharField(max_length=10, null=False)

    # Time when the branch was created
    br_created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # Time when the branch was last updated
    br_updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)

        # Created By
    br_created_by = models.CharField(max_length=255, null=True, blank=True)

    # Updated By
    br_updated_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.br_name

    class Meta:
        db_table = "branch"


"""
    Model representing Lab.
"""


class Lab(models.Model):
    # Primary key for the lab
    lab_id = models.AutoField(primary_key=True)

    # Name of the lab
    lab_name = models.CharField(max_length=255, unique=True, null=False)

    lab_code = models.CharField(max_length=10, unique=True, null=False)

    lab_state_code = models.CharField(max_length=10, unique=True, null=False)

    # Location of the lab
    lab_location = models.CharField(max_length=255)

    # Contact information for the lab
    lab_contact = models.CharField(
        max_length=10,
        unique=True,
        validators=[MinLengthValidator(10), MaxLengthValidator(10)],
    )

    # Address of the lab
    lab_address = models.TextField()

    # Email of the lab
    lab_email = models.EmailField(unique=True, null=False)

    # Post code of the lab
    lab_post_code = models.CharField(max_length=255)

    # Time when the lab was created
    lab_created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # Time when the lab was last updated
    lab_updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.lab_name

    class Meta:
        db_table = "lab"


class Roles(models.Model):
    """
    Model representing the roles in the system.
    """

    # Unique identifier for the role
    role_id = models.AutoField(primary_key=True)

    # Name of the role
    role_name = models.CharField(max_length=25, unique=True, null=False)

    # Description of the role
    role_desc = models.TextField()

    """
        Returns a string representation of the role.
    """

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = "roles"


class Mode(models.Model):
    mode_id = models.AutoField(primary_key=True)

    mode_name = models.CharField(max_length=255, unique=True, null=False)

    mode_code = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return self.mode_name

    class Meta:
        db_table = "mode"
        ordering = ["mode_id"]


class Entity(models.Model):
    """
    Model representing Entity.
    """

    # Primary key for the entity
    entity_id = models.AutoField(primary_key=True)

    # Name of the entity
    entity_name = models.CharField(max_length=255, unique=True, null=False)

    entity_code = models.CharField(max_length=10, unique=True, null=False)

    # Description of the entity
    entity_desc = models.TextField()

    entity_remarks = models.TextField()

    def __str__(self):
        return self.entity_name

    class Meta:
        db_table = "entity"


class EntityHistory(models.Model):
    """
    Model representing Entity History.
    """

    # Primary key for the entity history
    eh_id = models.AutoField(primary_key=True)

    # Foreign key to the entity
    eh_enid = models.ForeignKey(Entity, on_delete=models.CASCADE)

    # Operation performed on the entity
    eh_operation = models.CharField(max_length=255)

    # Employee ID associated with the operation
    eh_empid = models.IntegerField()

    # Date of the operation
    eh_operationdate = models.DateTimeField()

    # Record ID of the entity
    eh_recordid = models.IntegerField()

    status = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Entity History ID: {self.eh_id}"

    class Meta:
        db_table = "entity_history"


class EntityRolesRights(models.Model):
    """
    Model representing EntityRolesRights.
    """

    # Primary key for the entity roles rights
    ent_rnr_id = models.AutoField(primary_key=True)

    # Foreign key to the Entity table
    ent_rnr_entity_id = models.ForeignKey(Entity, on_delete=models.CASCADE, null=False)

    # Foreign key to the Roles table
    ent_rnr_role_id = models.ForeignKey(Roles, on_delete=models.CASCADE, null=False)

    ent_rnr_role_code = models.CharField(max_length=10, unique=True, null=False)

    ent_rnr_entity_code = models.CharField(max_length=10, unique=True, null=False)

    ent_rnr_read = models.BooleanField(default=False)

    ent_rnr_write = models.BooleanField(default=False)

    ent_rnr_update = models.BooleanField(default=False)

    ent_rnr_delete = models.BooleanField(default=False)

    ent_rnr_list = models.BooleanField(default=False)

    ent_rnr_approve = models.BooleanField(default=False)

    ent_rnr_cancel = models.BooleanField(default=False)

    ent_rnr_signature = models.BooleanField(default=False)

    def __str__(self):
        return self.ent_rnr_id

    class Meta:
        db_table = "entity_roles_rights"


class Basis(models.Model):
    """
    Model representing Basis.
    """

    # Primary key for the basis
    basis_id = models.AutoField(primary_key=True)

    # Foreign key to the TenantMaster table
    fk_tenant_id = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)

    # Code of the basis
    basis_code = models.CharField(max_length=225, unique=True, null=False)

    # Name of the basis
    basis_name = models.CharField(max_length=255, unique=True, null=False)

    # Time when the basis was created
    basis_created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # Time when the basis was last updated
    basis_updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    # Created By
    basis_created_by = models.CharField(max_length=255, null=True, blank=True)

    # Updated By
    basis_updated_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.basis_name

    class Meta:
        db_table = "basis"

class CommoditySpecs(models.Model):
    """
    Model representing CS.
    """

    # Primary key for the CS
    cs_id = models.AutoField(primary_key=True)

    # Foreign key to the TenantMaster table
    fk_tenant_id = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)

    # Tenant code
    tenant_code = models.CharField(max_length=10, null=False)

    # Foreign key to the Commodity table
    fk_cmd_id = models.ForeignKey(Commodity, on_delete=models.CASCADE)

    # Foreign key to the Parameter table
    fk_parameter_id = models.ForeignKey(Parameter, on_delete=models.CASCADE)

    # Foreign key to the Basis table
    fk_basis_id = models.ForeignKey(Basis, on_delete=models.CASCADE)

    # Foreign key to the Standard table
    fk_std_id = models.ForeignKey(Standard, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cs_id)

    class Meta:
        db_table = "commodity_specs"


