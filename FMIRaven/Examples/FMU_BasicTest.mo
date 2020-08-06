within FMIRaven.Examples;
model FMU_BasicTest
  FMUs.FMIRaven_Models_LorenzSystem_Parameters_fmu Parameters
    annotation (Placement(transformation(extent={{-10,18},{10,38}})));
  FMUs.FMIRaven_Models_LorenzSystem_Inputs_fmu Inputs(
    sigma=10,
    rho=28,
    beta=8/3) annotation (Placement(transformation(extent={{-10,-10},{10,10}})));
  FMUs.FMIRaven_Models_LorenzSystem_Connectors_fmu Connectors
    annotation (Placement(transformation(extent={{-10,-40},{10,-20}})));
  Modelica.Blocks.Sources.Constant sigma(k=10)
    annotation (Placement(transformation(extent={{-80,20},{-60,40}})));
  Modelica.Blocks.Sources.Constant rho(k=28)
    annotation (Placement(transformation(extent={{-80,-10},{-60,10}})));
  Modelica.Blocks.Sources.Constant beta(k=8/3)
    annotation (Placement(transformation(extent={{-80,-40},{-60,-20}})));
equation
  connect(sigma.y, Connectors.sigma) annotation (Line(points={{-59,30},{-20,30},
          {-20,-25},{-10.4,-25}}, color={0,0,127}));
  connect(rho.y, Connectors.rho) annotation (Line(points={{-59,0},{-30,0},{-30,
          -30},{-10.4,-30}}, color={0,0,127}));
  connect(beta.y, Connectors.beta) annotation (Line(points={{-59,-30},{-40,-30},
          {-40,-35},{-10.4,-35}}, color={0,0,127}));
  annotation (Icon(coordinateSystem(preserveAspectRatio=false)), Diagram(
        coordinateSystem(preserveAspectRatio=false)));
end FMU_BasicTest;
