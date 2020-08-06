within FMIRaven.Examples;
model FMU_Connectors
  FMUs.FMIRaven_Models_LorenzSystem_Connectors_fmu fmu
    annotation (Placement(transformation(extent={{-10,-10},{10,10}})));
  Modelica.Blocks.Sources.Constant sigma(k=10)
    annotation (Placement(transformation(extent={{-80,20},{-60,40}})));
  Modelica.Blocks.Sources.Constant rho(k=28)
    annotation (Placement(transformation(extent={{-80,-10},{-60,10}})));
  Modelica.Blocks.Sources.Constant beta(k=8/3)
    annotation (Placement(transformation(extent={{-80,-40},{-60,-20}})));
equation
  connect(sigma.y, fmu.sigma) annotation (Line(points={{-59,30},{-30,30},{-30,5},
          {-10.4,5}}, color={0,0,127}));
  connect(rho.y, fmu.rho)
    annotation (Line(points={{-59,0},{-10.4,0}}, color={0,0,127}));
  connect(beta.y, fmu.beta) annotation (Line(points={{-59,-30},{-30,-30},{-30,
          -5},{-10.4,-5}}, color={0,0,127}));
  annotation (Icon(coordinateSystem(preserveAspectRatio=false)), Diagram(
        coordinateSystem(preserveAspectRatio=false)),
    experiment(StopTime=100, __Dymola_Algorithm="Dassl"));
end FMU_Connectors;
